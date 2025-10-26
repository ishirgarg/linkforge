"""
Simple test script for MCP Documentation Server
Tests processing one URL and querying it using MCP SDK
"""

import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# For direct testing without MCP client, we'll use the functions directly
import sys
sys.path.insert(0, '.')
from mcp_server import process_documentation_url, query_documentation, get_processing_status, list_collections

async def test_with_direct_calls():
    """Test by calling the tool functions directly."""
    print("🧪 Testing MCP Documentation Server (Direct Function Calls)")
    print("=" * 60)
    
    # Test 1: Process documentation URL
    print("\n📚 Test 1: Processing documentation URL...")
    print("URL: https://docs.streamlit.io/develop/api-reference")
    print("Max URLs: 1")
    print("Crawler Workers: 200")
    
    result = await process_documentation_url(
        url="https://docs.streamlit.io/develop/api-reference",
        max_urls=1,
        crawler_workers=200
    )
    
    print("\nResponse:")
    print(result)
    
    # Extract job_id and collection_name
    lines = result.split('\n')
    job_id = None
    collection_name = None
    
    for line in lines:
        if line.startswith("Job ID:"):
            job_id = line.split("Job ID:")[1].strip()
        elif line.startswith("Collection:"):
            collection_name = line.split("Collection:")[1].strip()
    
    if job_id and collection_name:
        print(f"\n✅ Job started: {job_id}")
        print(f"✅ Collection: {collection_name}")
        
        # Test 2: Check status
        print("\n⏳ Test 2: Checking processing status...")
        print("Waiting for processing to complete...")
        
        for i in range(60):  # Wait up to 60 seconds
            await asyncio.sleep(1)
            status_result = await get_processing_status(job_id=job_id)
            
            if "COMPLETED" in status_result:
                print("\n✅ Processing completed!")
                print(status_result)
                break
            elif "FAILED" in status_result:
                print("\n❌ Processing failed!")
                print(status_result)
                return
            else:
                if i % 5 == 0:  # Print every 5 seconds
                    print(f"  Status check {i+1}/60... still processing")
        
        # Test 3: Query the documentation
        print("\n🔍 Test 3: Querying documentation...")
        query = "how to use st.header"
        print(f"Query: '{query}'")
        
        query_result = await query_documentation(
            query=query,
            collection_name=collection_name,
            max_results=2
        )
        
        print("\nQuery Response:")
        print(query_result)
        
        # Test 4: List collections
        print("\n📋 Test 4: Listing collections...")
        list_result = await list_collections()
        print(list_result)
        
        print("\n🎉 All tests completed!")
    else:
        print("\n❌ Could not extract job_id or collection_name from response")

if __name__ == "__main__":
    print("🧪 MCP Documentation Server Test")
    print("This test calls the tool functions directly (no HTTP required)")
    print()
    
    try:
        asyncio.run(test_with_direct_calls())
    except KeyboardInterrupt:
        print("\n\n⚠️ Test interrupted by user")
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()

