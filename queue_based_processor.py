"""
Queue-Based Multi-Model Gemini Processor
Processes multiple documents concurrently with chunk queues and immediate failover.

THREADING MODEL:
- Multiple worker threads (1-3 per model based on RPM)
- Three priority queues: high (first chunks), normal (middle), low (last chunks)
- Per-model locks for rate limiting (model.lock)
- Global lock for document status (document_status_lock)
- Global lock for statistics (stats_lock)

RACE CONDITION PREVENTION:
1. Atomic Rate Limit Reservation: Reserve API slot BEFORE making request
2. Minimal Lock Holding: Release locks before expensive I/O operations
3. Source Queue Tracking: Track which queue task came from for task_done()
4. Status Check Before Write: Prevent multiple threads from writing same document
5. Slot Cleanup on Failure: Remove reserved slot if API call fails
"""

import os
import json
import requests
import time
import random
import threading
import queue
from typing import List, Dict, Any, Optional, Tuple
from pathlib import Path
from dotenv import load_dotenv
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from enum import Enum

# Load environment variables
load_dotenv()

# Import vector database manager
try:
    from vector_db import ChromaVectorDB
    VECTOR_DB_AVAILABLE = True
except ImportError:
    VECTOR_DB_AVAILABLE = False
    print("⚠️ ChromaVectorDB not available. Install chromadb and sentence-transformers to enable vector database features.")

class ModelStatus(Enum):
    AVAILABLE = "available"
    RATE_LIMITED = "rate_limited"
    ERROR = "error"
    BUSY = "busy"

@dataclass
class ChunkTask:
    """Represents a chunk processing task."""
    chunk_id: str
    content: str
    url: str
    is_first: bool
    is_last: bool
    chunk_index: int
    total_chunks: int
    retry_count: int = 0
    max_retries: int = 10  # Maximum retries before giving up

@dataclass
class ModelInfo:
    """Information about a Gemini model."""
    name: str
    base_url: str
    rpm: int
    status: ModelStatus = ModelStatus.AVAILABLE
    calls: List[float] = None
    lock: threading.Lock = None
    last_error: Optional[str] = None
    error_count: int = 0
    
    def __post_init__(self):
        if self.calls is None:
            self.calls = []
        if self.lock is None:
            self.lock = threading.Lock()

class QueueBasedProcessor:
    def __init__(self, api_key: str = None, max_retries: int = 10, enable_vector_db: bool = True, 
                 collection_name: str = "documentation", workers_per_model: int = None):
        """
        Initialize the queue-based processor with correct model names.
        
        Args:
            api_key: Optional API key (otherwise loads from env)
            max_retries: Maximum retries for failed chunks
            enable_vector_db: Enable ChromaDB integration for embeddings
            collection_name: Name of the ChromaDB collection
            workers_per_model: Number of workers per model (default: auto-calculated from RPM)
        """
        # Load all available API keys
        self.api_keys = []
        if api_key:
            self.api_keys.append(api_key)
        else:
            # Load primary key
            primary_key = os.getenv('GEMINI_API_KEY')
            if primary_key:
                self.api_keys.append(primary_key)
            
            # Load additional keys (GEMINI_API_KEY_1, GEMINI_API_KEY_2, etc.)
            i = 1
            while True:
                additional_key = os.getenv(f'GEMINI_API_KEY_{i}')
                if additional_key:
                    self.api_keys.append(additional_key)
                    i += 1
                else:
                    break
        
        if not self.api_keys:
            raise ValueError("No GEMINI_API_KEY found in environment variables")
        
        print(f"🔑 Loaded {len(self.api_keys)} API key(s)")
        
        self.max_retries = max_retries
        self.api_key_lock = threading.Lock()  # Lock for thread-safe random selection
        self.workers_per_model = workers_per_model  # Custom worker count per model
        
        # Initialize Vector Database
        self.enable_vector_db = enable_vector_db and VECTOR_DB_AVAILABLE
        self.vector_db = None
        
        if self.enable_vector_db:
            try:
                self.vector_db = ChromaVectorDB(
                    path="./chroma_db",
                    collection_name=collection_name,
                    chunk_size=500,  # Words per chunk
                    chunk_overlap=50  # Overlapping words
                )
                print(f"✅ Vector database enabled (Qwen 0.6B embeddings)")
                print(f"   Collection: {collection_name}")
                print(f"   Chunk size: 500 words with 50 word overlap")
            except Exception as e:
                print(f"⚠️ Could not initialize vector database: {str(e)}")
                print(f"   Make sure sentence-transformers is installed")
                print(f"   Install with: pip install sentence-transformers")
                self.enable_vector_db = False
        elif enable_vector_db and not VECTOR_DB_AVAILABLE:
            print(f"⚠️ Vector database requested but dependencies not installed")
            print(f"   Install with: pip install chromadb sentence-transformers")
        
        # Correct model configurations (based on your actual rate limits)
        self.models = {
            'gemini-2.0-flash-lite': ModelInfo(
                name='gemini-2.0-flash-lite',
                base_url='https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-lite:generateContent',
                rpm=30
            ),
            'gemini-2.5-flash-lite': ModelInfo(
                name='gemini-2.5-flash-lite',
                base_url='https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:generateContent',
                rpm=15
            ),
            'gemini-2.5-flash': ModelInfo(
                name='gemini-2.5-flash',
                base_url='https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent',
                rpm=10
            ),
            'gemini-2.0-flash-exp': ModelInfo(
                name='gemini-2.0-flash-exp',
                base_url='https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-exp:generateContent',
                rpm=10
            ),
            'gemini-2.0-flash': ModelInfo(
                name='gemini-2.0-flash',
                base_url='https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent',
                rpm=15
            ),
            'gemini-2.5-pro': ModelInfo(
                name='gemini-2.5-pro',
                base_url='https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-pro:generateContent',
                rpm=2
            ),
            'learnlm-2.0-flash-experimental': ModelInfo(
                name='learnlm-2.0-flash-experimental',
                base_url='https://generativelanguage.googleapis.com/v1beta/models/learnlm-2.0-flash-experimental:generateContent',
                rpm=15
            )
        }
        
        # Queues for different priority levels
        self.high_priority_queue = queue.Queue()  # For first chunks (need titles)
        self.normal_priority_queue = queue.Queue()  # For middle chunks
        self.low_priority_queue = queue.Queue()  # For last chunks
        
        # Results storage
        self.results = {}
        self.results_lock = threading.Lock()
        
        # Statistics
        self.stats = {
            'total_processed': 0,
            'successful': 0,
            'failed': 0,
            'rate_limited': 0,
            'model_switches': 0
        }
        self.stats_lock = threading.Lock()
        
        # Create output directory
        self.output_dir = Path("documentation_markdown")
        self.output_dir.mkdir(exist_ok=True)
        
        # Start worker threads
        self.workers = []
        self.shutdown_event = threading.Event()
        
        print("🚀 Queue-Based Multi-Model Processor initialized!")
        print(f"📁 Output directory: {self.output_dir}")
        print(f"⚡ Total theoretical throughput: {sum(m.rpm for m in self.models.values())} calls/minute")
        print(f"🤖 Available models: {len(self.models)}")
        for model_name, model_info in self.models.items():
            print(f"  - {model_name}: {model_info.rpm} RPM")
        
        # Start worker threads
        self._start_workers()
    
    def _start_workers(self):
        """Start worker threads for each model."""
        for model_name in self.models.keys():
            # Use custom worker count or auto-calculate based on RPM
            if self.workers_per_model:
                worker_count = self.workers_per_model
            else:
                # Use more workers for higher RPM models
                rpm = self.models[model_name].rpm
                worker_count = max(1, min(3, rpm // 5))  # 1-3 workers based on RPM
            
            for i in range(worker_count):
                worker = threading.Thread(
                    target=self._worker_loop,
                    args=(model_name,),
                    daemon=True
                )
                worker.start()
                self.workers.append(worker)
        
        print(f"🔄 Started {len(self.workers)} worker threads")
    
    def _get_random_api_key(self) -> str:
        """Get a random API key for load balancing across keys."""
        with self.api_key_lock:
            return random.choice(self.api_keys)
    
    def _clean_old_calls(self, model_name: str):
        """Remove API calls older than 1 minute. Should be called while holding model.lock."""
        model = self.models[model_name]
        # Note: This method assumes the caller already holds model.lock
        # to avoid double-locking and reduce contention
        current_time = time.time()
        model.calls = [call_time for call_time in model.calls if current_time - call_time < 60]
    
    def _is_model_available(self, model_name: str) -> bool:
        """Check if a model is available for processing."""
        model = self.models[model_name]
        
        with model.lock:
            # Clean old calls first (while holding lock)
            self._clean_old_calls(model_name)
            
            if model.status == ModelStatus.ERROR:
                # Check if we should retry after error
                if time.time() - model.last_error > 300:  # 5 minutes
                    model.status = ModelStatus.AVAILABLE
                    model.error_count = 0
                    model.last_error = None
                else:
                    return False
            
            # Check current rate limit status
            current_calls = len(model.calls)
            
            if current_calls >= model.rpm:
                # Model is rate limited
                model.status = ModelStatus.RATE_LIMITED
                return False
            else:
                # Model is available
                model.status = ModelStatus.AVAILABLE
                return True
    
    def _get_available_model(self, priority: str = "normal") -> Optional[str]:
        """Get the best available model based on priority and availability."""
        # Sort models by preference (higher RPM first)
        sorted_models = sorted(
            self.models.items(),
            key=lambda x: x[1].rpm,
            reverse=True
        )
        
        for model_name, model_info in sorted_models:
            if self._is_model_available(model_name):
                return model_name
        
        return None
    
    def _wait_for_availability(self, model_name: str, timeout: float = 30.0) -> bool:
        """Wait for a model to become available."""
        start_time = time.time()
        
        while time.time() - start_time < timeout:
            if self._is_model_available(model_name):
                return True
            time.sleep(0.1)
        
        return False
    
    def _make_api_request(self, task: ChunkTask, model_name: str) -> Tuple[bool, str]:
        """Make an API request to the specified model."""
        model = self.models[model_name]
        
        # Atomically reserve a slot in the rate limit (prevents race conditions)
        with model.lock:
            self._clean_old_calls(model_name)
            
            if len(model.calls) >= model.rpm:
                model.status = ModelStatus.RATE_LIMITED
                return False, f"Model {model_name} rate limited"
            
            # Reserve the slot BEFORE making the request
            model.calls.append(time.time())
        
        # Create prompt based on chunk position
        prompt = self._create_prompt(task)
        
        # Get a random API key for this request (load balancing)
        api_key = self._get_random_api_key()
        headers = {
            'Content-Type': 'application/json',
            'X-goog-api-key': api_key
        }
        
        try:
            # Make API request
            response = requests.post(
                model.base_url,
                headers=headers,
                json={
                    "contents": [
                        {
                            "parts": [
                                {
                                    "text": prompt
                                }
                            ]
                        }
                    ],
                    "generationConfig": {
                        "temperature": 0.1,
                        "topP": 0.8,
                        "topK": 10
                    }
                },
                timeout=60
            )
            
            if response.status_code == 200:
                result = response.json()
                
                # Validate response
                if 'candidates' not in result or len(result['candidates']) == 0:
                    raise Exception(f"Invalid response: {result}")
                
                candidate = result['candidates'][0]
                if 'content' not in candidate or 'parts' not in candidate['content'] or len(candidate['content']['parts']) == 0:
                    raise Exception(f"Invalid candidate structure: {candidate}")
                
                if 'text' not in candidate['content']['parts'][0]:
                    raise Exception(f"Missing text in response: {candidate['content']['parts'][0]}")
                
                markdown_content = candidate['content']['parts'][0]['text']
                
                # Update status (slot already reserved)
                with model.lock:
                    if len(model.calls) >= model.rpm:
                        model.status = ModelStatus.RATE_LIMITED
                    else:
                        model.status = ModelStatus.AVAILABLE
                
                # Update statistics
                with self.stats_lock:
                    self.stats['successful'] += 1
                
                return True, markdown_content
                
            elif response.status_code == 429:  # Rate limited
                # Remove the reserved slot since we didn't actually use it
                with model.lock:
                    if model.calls:
                        model.calls.pop()
                    model.status = ModelStatus.RATE_LIMITED
                with self.stats_lock:
                    self.stats['rate_limited'] += 1
                return False, f"Rate limited: {response.status_code}"
                
            else:
                # Remove the reserved slot on error
                with model.lock:
                    if model.calls:
                        model.calls.pop()
                error_msg = f"API Error {response.status_code}: {response.text}"
                model.status = ModelStatus.ERROR
                model.last_error = time.time()
                model.error_count += 1
                return False, error_msg
                
        except requests.exceptions.Timeout:
            # Remove the reserved slot on timeout
            with model.lock:
                if model.calls:
                    model.calls.pop()
            error_msg = "Request timed out"
            model.status = ModelStatus.ERROR
            model.last_error = time.time()
            model.error_count += 1
            return False, error_msg
            
        except Exception as e:
            # Remove the reserved slot on exception
            with model.lock:
                if model.calls:
                    model.calls.pop()
            error_msg = f"Request failed: {str(e)}"
            model.status = ModelStatus.ERROR
            model.last_error = time.time()
            model.error_count += 1
            return False, error_msg
    
    def _create_prompt(self, task: ChunkTask) -> str:
        """Create a prompt for the given task."""
        if task.is_first and task.is_last:
            return f"""
            Convert the following HTML content from a documentation page into clean, well-structured markdown.
            
            URL: {task.url}
            
            Requirements:
            1. Extract the main content and structure
            2. Convert headings, lists, code blocks, and links properly
            3. Remove navigation elements, sidebars, and non-content elements
            4. Create a clear hierarchy with proper markdown headings
            5. Preserve code examples and technical details
            6. Make it readable and well-formatted
            7. Add a title at the top based on the page content
            8. Include the original URL as a reference
            
            HTML Content:
            {task.content}
            """
        elif task.is_first:
            return f"""
            Convert the following HTML content (first part of {task.total_chunks}) from a documentation page into clean, well-structured markdown.
            
            URL: {task.url}
            
            Requirements:
            1. Extract the main content and structure
            2. Convert headings, lists, code blocks, and links properly
            3. Remove navigation elements, sidebars, and non-content elements
            4. Create a clear hierarchy with proper markdown headings
            5. Preserve code examples and technical details
            6. Make it readable and well-formatted
            7. Add a title at the top based on the page content
            8. Include the original URL as a reference
            9. This is the FIRST part - include the main title and introduction
            
            HTML Content:
            {task.content}
            """
        elif task.is_last:
            return f"""
            Convert the following HTML content (last part of {task.total_chunks}) from a documentation page into clean, well-structured markdown.
            
            URL: {task.url}
            
            Requirements:
            1. Extract the main content and structure
            2. Convert headings, lists, code blocks, and links properly
            3. Remove navigation elements, sidebars, and non-content elements
            4. Create a clear hierarchy with proper markdown headings
            5. Preserve code examples and technical details
            6. Make it readable and well-formatted
            7. This is the LAST part - include conclusion and final sections
            8. Do NOT include a title (it should be in the first chunk)
            
            HTML Content:
            {task.content}
            """
        else:
            return f"""
            Convert the following HTML content (part {task.chunk_index} of {task.total_chunks}) from a documentation page into clean, well-structured markdown.
            
            URL: {task.url}
            
            Requirements:
            1. Extract the main content and structure
            2. Convert headings, lists, code blocks, and links properly
            3. Remove navigation elements, sidebars, and non-content elements
            4. Create a clear hierarchy with proper markdown headings
            5. Preserve code examples and technical details
            6. Make it readable and well-formatted
            7. This is a MIDDLE part - continue the content flow
            8. Do NOT include a title (it should be in the first chunk)
            
            HTML Content:
            {task.content}
            """
    
    def _worker_loop(self, model_name: str):
        """Worker loop for processing chunks."""
        while not self.shutdown_event.is_set():
            try:
                # Try to get a task from any queue (prioritize high priority)
                task = None
                source_queue = None
                for queue_obj in [self.high_priority_queue, self.normal_priority_queue, self.low_priority_queue]:
                    try:
                        task = queue_obj.get(timeout=1.0)
                        source_queue = queue_obj
                        break
                    except queue.Empty:
                        continue
                
                if task is None:
                    continue
                
                # Print queue status when picking up a task
                try:
                    total_queued = self.high_priority_queue.qsize() + self.normal_priority_queue.qsize() + self.low_priority_queue.qsize()
                    print(f"📋 {model_name}: Processing {task.chunk_id} (Queue: {total_queued} remaining)")
                except:
                    pass
                
                # Process the task
                success, result = self._make_api_request(task, model_name)
                
                if success:
                    # Store successful result in document status
                    should_write = False
                    doc_url = None
                    
                    with self.document_status_lock:
                        if task.url in self.document_status:
                            self.document_status[task.url]['chunks'][task.chunk_id] = result
                            self.document_status[task.url]['completed_chunks'] += 1
                            
                            # Check if document is complete
                            total_chunks = self.document_status[task.url]['total_chunks']
                            completed = self.document_status[task.url]['completed_chunks']
                            if completed >= total_chunks and self.document_status[task.url]['status'] != 'completed':
                                self.document_status[task.url]['status'] = 'completed'
                                should_write = True
                                doc_url = task.url
                    
                    # Write file OUTSIDE the lock to avoid blocking other workers
                    if should_write:
                        self._write_completed_document(doc_url)
                    
                    print(f"✅ {model_name}: {task.chunk_id} completed")
                    
                else:
                    # Handle failure - immediately try with different model
                    print(f"⚠️ {model_name}: {task.chunk_id} failed, switching to another model: {result}")
                    
                    # Try with next available model immediately
                    success_with_other = False
                    available_models = [name for name in self.models.keys() 
                                      if name != model_name and self._is_model_available(name)]
                    
                    if available_models:
                        for other_model_name in available_models:
                            print(f"🔄 Switching to {other_model_name} for {task.chunk_id}")
                            success, result = self._make_api_request(task, other_model_name)
                            if success:
                                # Store successful result in document status
                                should_write = False
                                doc_url = None
                                
                                with self.document_status_lock:
                                    if task.url in self.document_status:
                                        self.document_status[task.url]['chunks'][task.chunk_id] = result
                                        self.document_status[task.url]['completed_chunks'] += 1
                                        
                                        # Check if document is complete
                                        total_chunks = self.document_status[task.url]['total_chunks']
                                        completed = self.document_status[task.url]['completed_chunks']
                                        if completed >= total_chunks and self.document_status[task.url]['status'] != 'completed':
                                            self.document_status[task.url]['status'] = 'completed'
                                            should_write = True
                                            doc_url = task.url
                                
                                # Write file OUTSIDE the lock
                                if should_write:
                                    self._write_completed_document(doc_url)
                                
                                print(f"✅ {other_model_name}: {task.chunk_id} completed")
                                success_with_other = True
                                
                                # Track model switch
                                with self.stats_lock:
                                    self.stats['model_switches'] += 1
                                break
                    else:
                        print(f"⚠️ No available models for {task.chunk_id} - all models are rate limited or in error")
                    
                    if not success_with_other:
                        # All models failed - check if we should retry or give up
                        task.retry_count += 1
                        
                        if task.retry_count < task.max_retries:
                            # Put back in queue for retry
                            print(f"⚠️ All models failed for {task.chunk_id}, retry {task.retry_count}/{task.max_retries}, putting back in queue: {result}")
                            
                            # Track retry
                            with self.stats_lock:
                                self.stats['retries'] += 1
                            
                            # Mark current task as done BEFORE re-queuing
                            if source_queue is not None:
                                source_queue.task_done()
                            
                            # Add exponential backoff delay before retrying (non-blocking)
                            delay = min(5, 2 ** task.retry_count)  # Max 5 seconds delay
                            time.sleep(delay)
                            
                            # Put back in appropriate queue for retry (this adds a new task)
                            if task.is_first:
                                self.high_priority_queue.put(task)
                            elif task.is_last:
                                self.low_priority_queue.put(task)
                            else:
                                self.normal_priority_queue.put(task)
                            
                            # Continue without calling task_done() again (already called above)
                            continue
                        else:
                            # Max retries exceeded - store error result
                            error_result = f"# Error Processing Chunk {task.chunk_index}\n\nFailed after {task.max_retries} retries.\n\nError: {result}"
                            with self.document_status_lock:
                                if task.url in self.document_status:
                                    self.document_status[task.url]['chunks'][task.chunk_id] = error_result
                                    self.document_status[task.url]['completed_chunks'] += 1
                                    
                                    # Check if document is complete
                                    total_chunks = self.document_status[task.url]['total_chunks']
                                    completed = self.document_status[task.url]['completed_chunks']
                                    if completed >= total_chunks:
                                        self.document_status[task.url]['status'] = 'completed'
                                        # Write file immediately when document is complete
                                        self._write_completed_document(task.url)
                            
                            print(f"❌ Max retries exceeded for {task.chunk_id}, giving up: {result}")
                        
                        with self.stats_lock:
                            self.stats['failed'] += 1
                
                # Mark task as done in the source queue
                if source_queue is not None:
                    source_queue.task_done()
                
            except Exception as e:
                print(f"❌ Worker {model_name} error: {str(e)}")
                time.sleep(1)
    
    def chunk_html_content(self, html_content: str, max_chunk_size: int = 8000) -> List[str]:
        """Chunk HTML content for processing."""
        if len(html_content) <= max_chunk_size:
            return [html_content]
        
        import re
        
        # Detect if this is HTML or markdown-like content
        is_html = bool(re.search(r'<[^>]+>', html_content))
        
        if is_html:
            heading_pattern = r'(<h[1-3][^>]*>.*?</h[1-3]>)'
            parts = re.split(heading_pattern, html_content, flags=re.IGNORECASE | re.DOTALL)
        else:
            heading_pattern = r'(^#{1,3}\s+.*$)'
            parts = re.split(heading_pattern, html_content, flags=re.MULTILINE)
        
        chunks = []
        current_chunk = ""
        
        for part in parts:
            if len(current_chunk + part) <= max_chunk_size:
                current_chunk += part
            else:
                if current_chunk:
                    chunks.append(current_chunk.strip())
                current_chunk = part
        
        if current_chunk:
            chunks.append(current_chunk.strip())
        
        # Further split large chunks
        final_chunks = []
        for chunk in chunks:
            if len(chunk) <= max_chunk_size:
                final_chunks.append(chunk)
            else:
                # Split by paragraphs
                para_pattern = r'(\n\s*\n)'
                parts = re.split(para_pattern, chunk)
                
                sub_chunks = []
                current = ""
                for part in parts:
                    if len(current + part) <= max_chunk_size:
                        current += part
                    else:
                        if current:
                            sub_chunks.append(current.strip())
                        current = part
                if current:
                    sub_chunks.append(current.strip())
                
                final_chunks.extend(sub_chunks)
        
        return final_chunks
    
    
    def _combine_chunks(self, processed_chunks: List[str], url: str) -> str:
        """Combine processed chunks into a single markdown document."""
        print(f"🔗 Combining {len(processed_chunks)} chunks...")
        
        # Filter out error chunks
        valid_chunks = []
        error_chunks = []
        
        for i, chunk in enumerate(processed_chunks):
            if chunk.startswith('# Error Processing Chunk'):
                error_chunks.append(i + 1)
            else:
                valid_chunks.append((i, chunk))
        
        if error_chunks:
            print(f"⚠️ Warning: {len(error_chunks)} chunks failed: {error_chunks}")
        
        if not valid_chunks:
            return f"# Error Processing Page\n\nAll chunks failed to process for: {url}"
        
        # Start with first valid chunk
        combined = valid_chunks[0][1]
        
        # Add subsequent chunks, removing duplicate titles
        for i, chunk in valid_chunks[1:]:
            lines = chunk.split('\n')
            filtered_lines = []
            skip_title = True
            
            for line in lines:
                if skip_title and (line.startswith('# ') or line.startswith('**Original URL:**')):
                    continue
                elif line.startswith('---') and skip_title:
                    skip_title = False
                    continue
                else:
                    skip_title = False
                    filtered_lines.append(line)
            
            if filtered_lines:
                combined += '\n\n' + '\n'.join(filtered_lines)
        
        if error_chunks:
            combined += f"\n\n---\n\n**Note:** Some sections failed to process (chunks {', '.join(map(str, error_chunks))})."
        
        print(f"✅ Successfully combined {len(valid_chunks)} valid chunks")
        return combined
    
    def process_multiple_documents(self, documents: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Process multiple documents concurrently by adding all chunks to queues."""
        print(f"🚀 Processing {len(documents)} documents concurrently...")
        
        # Clear previous results
        with self.results_lock:
            self.results.clear()
        
        # Reset statistics
        with self.stats_lock:
            self.stats = {
                'total_processed': 0,
                'successful': 0,
                'failed': 0,
                'rate_limited': 0,
                'model_switches': 0,
                'retries': 0
            }
        
        # Document tracking
        self.document_status = {}
        self.document_status_lock = threading.Lock()
        
        # Add all documents to processing queues
        total_chunks = 0
        for i, doc in enumerate(documents, 1):
            url = doc['url']
            
            if doc['status'] == 'success' and doc.get('raw_result'):
                html_content = str(doc['raw_result'])
                chunks = self.chunk_html_content(html_content, max_chunk_size=8000)
                
                print(f"📄 Document {i}: {url} - {len(chunks)} chunks")
                
                # Track document status
                with self.document_status_lock:
                    self.document_status[url] = {
                        'index': i,
                        'total_chunks': len(chunks),
                        'completed_chunks': 0,
                        'chunks': {},
                        'status': 'processing'
                    }
                
                # Add all chunks to appropriate queues
                for j, chunk in enumerate(chunks):
                    task = ChunkTask(
                        chunk_id=f"{url}_chunk_{j+1}",
                        content=chunk,
                        url=url,
                        is_first=(j == 0),
                        is_last=(j == len(chunks) - 1),
                        chunk_index=j + 1,
                        total_chunks=len(chunks),
                        max_retries=self.max_retries
                    )
                    
                    # Add to appropriate queue based on priority
                    if j == 0:  # First chunk
                        self.high_priority_queue.put(task)
                    elif j == len(chunks) - 1:  # Last chunk
                        self.low_priority_queue.put(task)
                    else:  # Middle chunks
                        self.normal_priority_queue.put(task)
                    
                    total_chunks += 1
            else:
                print(f"⚠️ Skipping document {i}: {url} - no content or error")
                with self.document_status_lock:
                    self.document_status[url] = {
                        'index': i,
                        'total_chunks': 0,
                        'completed_chunks': 0,
                        'chunks': {},
                        'status': 'skipped'
                    }
        
        print(f"📊 Total chunks queued: {total_chunks}")
        print(f"⏳ Waiting for all chunks to be processed...")
        
        # Wait for all chunks to be processed
        self.high_priority_queue.join()
        self.normal_priority_queue.join()
        self.low_priority_queue.join()
        
        print("✅ All chunks processed, combining results...")
        
        # Combine results for each document
        processed_documents = []
        for doc in documents:
            url = doc['url']
            
            with self.document_status_lock:
                doc_status = self.document_status.get(url, {})
            
            if doc_status.get('status') == 'skipped':
                doc['markdown_content'] = f"# Error\n\nCould not process: {url}"
                doc['markdown_file'] = None
                doc['processed_at'] = time.time()
            else:
                # Document was processed - get the already-written file info
                if doc_status.get('status') == 'completed' and 'markdown_file' in doc_status:
                    # File was already written during processing
                    doc['markdown_content'] = doc_status.get('markdown_content', '')
                    doc['markdown_file'] = doc_status.get('markdown_file')
                    doc['processed_at'] = doc_status.get('written_at', time.time())
                    print(f"✅ Document {doc_status['index']} completed: {url} (already written)")
                else:
                    # Document wasn't completed or file wasn't written - create error
                    doc['markdown_content'] = f"# Error\n\nDocument processing incomplete: {url}"
                    doc['markdown_file'] = None
                    doc['processed_at'] = time.time()
                    print(f"⚠️ Document {doc_status['index']} incomplete: {url}")
            
            processed_documents.append(doc)
            
            with self.stats_lock:
                self.stats['total_processed'] += 1
        
        # Print final statistics
        self._print_statistics()
        
        return processed_documents
    
    def _write_completed_document(self, url: str):
        """Write a completed document to markdown file immediately."""
        # Get document data while holding lock (minimal time)
        with self.document_status_lock:
            doc_status = self.document_status.get(url, {})
            if doc_status.get('status') != 'completed':
                return
            
            # Copy data we need (fast operation)
            total_chunks = doc_status['total_chunks']
            chunks_dict = doc_status['chunks'].copy()
            doc_index = doc_status['index']
        
        # Do expensive operations OUTSIDE the lock
        chunk_results = []
        for i in range(total_chunks):
            chunk_id = f"{url}_chunk_{i+1}"
            if chunk_id in chunks_dict:
                chunk_results.append(chunks_dict[chunk_id])
            else:
                chunk_results.append(f"# Error Processing Chunk {i+1}\n\nChunk not processed.")
        
        # Combine all chunks (expensive)
        markdown_content = self._combine_chunks(chunk_results, url)
        
        # Save markdown file (I/O operation)
        filename = self._save_markdown(markdown_content, url, doc_index)
        
        # Update document status with file info (quick lock)
        with self.document_status_lock:
            if url in self.document_status:
                self.document_status[url]['markdown_file'] = filename
                self.document_status[url]['markdown_content'] = markdown_content
                self.document_status[url]['written_at'] = time.time()
        
        print(f"💾 Document {doc_index} written: {filename}")
        
        # Embed into vector database (if enabled)
        if self.enable_vector_db and self.vector_db:
            print(f"🔄 Starting embedding for document {doc_index}...")
            try:
                # Create a unique ID for this document
                doc_id = f"doc_{doc_index}_{url.split('/')[-1]}"
                print(f"   Document ID: {doc_id}")
                print(f"   Content length: {len(markdown_content)} characters")
                
                # Insert the markdown content (ChromaVectorDB will handle chunking)
                print(f"   Calling vector_db.insert()...")
                self.vector_db.insert(
                    documents=[markdown_content],
                    ids=[doc_id]
                )
                print(f"✅ Embedded document into vector DB (ID: {doc_id})")
            except Exception as e:
                print(f"❌ Vector DB embedding failed: {str(e)}")
                import traceback
                traceback.print_exc()

    def _save_markdown(self, markdown_content: str, url: str, index: int) -> str:
        """Save markdown content to a file."""
        url_parts = url.replace('https://', '').replace('http://', '').split('/')
        path_parts = url_parts[1:] if len(url_parts) > 1 else []
        
        clean_parts = []
        for part in path_parts:
            clean_part = part.replace('.html', '').replace('.htm', '')
            if clean_part and clean_part != 'index':
                clean_parts.append(clean_part)
        
        if clean_parts:
            filename = f"{index:03d}_{'_'.join(clean_parts)}.md"
        else:
            filename = f"{index:03d}_homepage.md"
        
        filename = "".join(c for c in filename if c.isalnum() or c in "._-")
        filepath = self.output_dir / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        print(f"💾 Saved: {filepath}")
        return str(filepath)
    
    def get_model_status(self) -> dict:
        """Get current status of all models."""
        status = {}
        for model_name, model_info in self.models.items():
            with model_info.lock:
                current_time = time.time()
                # Clean old calls
                if model_info.calls:
                    model_info.calls = [call_time for call_time in model_info.calls if current_time - call_time < 60]
                
                calls_made = len(model_info.calls) if model_info.calls else 0
                remaining = max(0, model_info.rpm - calls_made)
                
                # Update status based on current calls
                if calls_made >= model_info.rpm:
                    model_info.status = ModelStatus.RATE_LIMITED
                else:
                    model_info.status = ModelStatus.AVAILABLE
                
                status[model_name] = {
                    'status': model_info.status.value,
                    'calls_made': calls_made,
                    'rpm_limit': model_info.rpm,
                    'remaining': remaining,
                    'error_count': model_info.error_count,
                    'last_error': model_info.last_error,
                    'is_available': calls_made < model_info.rpm
                }
        return status

    def _print_statistics(self):
        """Print processing statistics."""
        with self.stats_lock:
            print(f"\n📊 Processing Statistics:")
            print(f"  - Total processed: {self.stats['total_processed']}")
            print(f"  - Successful: {self.stats['successful']}")
            print(f"  - Failed: {self.stats['failed']}")
            print(f"  - Rate limited: {self.stats['rate_limited']}")
            print(f"  - Model switches: {self.stats['model_switches']}")
            print(f"  - Retries: {self.stats['retries']}")
            
            # Show model usage with rate limits
            print(f"\n🤖 Model Status:")
            model_status = self.get_model_status()
            for model_name, status in model_status.items():
                print(f"  - {model_name}: {status['calls_made']}/{status['rpm_limit']} calls ({status['remaining']} remaining) - {status['status']}")
            
            # Show vector database stats
            if self.enable_vector_db and self.vector_db:
                print(f"\n🔍 Vector Database Stats:")
                try:
                    # Get collection count
                    count = self.vector_db.collection.count()
                    print(f"  - Total chunks: {count}")
                    print(f"  - Collection: {self.vector_db.collection.name}")
                    print(f"  - Embedding model: Qwen/Qwen3-Embedding-0.6B")
                    print(f"  - Chunk size: {self.vector_db.chunk_size} words")
                    print(f"  - Chunk overlap: {self.vector_db.chunk_overlap} words")
                except Exception as e:
                    print(f"  ⚠️ Could not retrieve stats: {str(e)}")
    
    def shutdown(self):
        """Shutdown the processor and stop all workers."""
        print("🛑 Shutting down processor...")
        self.shutdown_event.set()
        
        # Wait for workers to finish
        for worker in self.workers:
            worker.join(timeout=5.0)
        
        print("✅ Processor shutdown complete")


def main():
    """Example usage of the queue-based processor."""
    print("🚀 Queue-Based Multi-Model Gemini Processor")
    print("=" * 60)
    
    # Initialize processor
    processor = QueueBasedProcessor()
    
    try:
        # Load scraped data
        import glob
        result_files = glob.glob("manual_crawl_results_*.json")
        if not result_files:
            print("❌ No scraped data found. Please run manual_url_crawler.py first.")
            return
        
        latest_file = max(result_files, key=os.path.getctime)
        print(f"📂 Loading scraped data from: {latest_file}")
        
        with open(latest_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        scraped_data = data.get('scraped_data', [])
        if not scraped_data:
            print("❌ No scraped data found in the file.")
            return
        
        print(f"📊 Found {len(scraped_data)} pages to process")
        
        # Process all pages
        processed_data = processor.process_multiple_documents(scraped_data)
        
        # Save results
        timestamp = int(time.time())
        results_file = f"queue_processed_results_{timestamp}.json"
        
        with open(results_file, 'w', encoding='utf-8') as f:
            json.dump(processed_data, f, indent=2, ensure_ascii=False)
        
        print(f"\n✅ Queue-based processing completed!")
        print(f"📁 Markdown files saved to: {processor.output_dir}")
        print(f"💾 Full results saved to: {results_file}")
        
    finally:
        processor.shutdown()


if __name__ == "__main__":
    main()
