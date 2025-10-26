import React, { useState, useEffect } from "react";

export default function App() {
    const [url, setUrl] = useState("");
    const [loading, setLoading] = useState(false);
    const [jobId, setJobId] = useState(null);
    const [jobStatus, setJobStatus] = useState(null);
    const [error, setError] = useState(null);

    const MAX_URLS = 4;

    // Poll job status every second
    useEffect(() => {
        if (!jobId) return;

        const pollStatus = async () => {
            try {
                const res = await fetch(`http://localhost:8000/api/status/${jobId}`);
                if (res.ok) {
                    const data = await res.json();
                    setJobStatus(data);

                    // Stop polling if job is completed or failed
                    if (data.status === 'completed' || data.status === 'failed') {
                        setJobId(null);
                    }
                }
            } catch (err) {
                console.error('Status poll error:', err);
            }
        };

        // Poll immediately, then every second
        pollStatus();
        const interval = setInterval(pollStatus, 1000);

        return () => clearInterval(interval);
    }, [jobId]);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        setError(null);
        setJobStatus(null);

        try {
            // Parse URL to create valid collection name
            const parsedUrl = new URL(url);
            const collectionName = `docs_${parsedUrl.hostname.replace(/\./g, '_')}${parsedUrl.pathname.replace(/[^a-zA-Z0-9]/g, '_')}`.replace(/_+$/, '');

            const res = await fetch("http://localhost:8000/api/process", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    url: url,
                    max_urls: MAX_URLS,
                    collection_name: collectionName
                }),
            });

            if (!res.ok) {
                const text = await res.text();
                throw new Error(`${res.status} ${res.statusText}: ${text}`);
            }

            const data = await res.json();

            // Start polling
            setJobId(data.job_id);
        } catch (err) {
            console.error('Error details:', err);
            setError(err.message || 'Unknown error occurred');
        } finally {
            setLoading(false);
        }
    };

    const getStatusIcon = () => {
        if (!jobStatus) return "⏳";
        switch (jobStatus.status) {
            case 'completed': return "✅";
            case 'failed': return "❌";
            default: return "⏳";
        }
    };

    return (
        <div className="min-h-screen flex flex-col items-center justify-center bg-gradient-to-br from-indigo-50 via-purple-50 to-white p-6">
            <div className="w-full max-w-2xl bg-white rounded-3xl shadow-2xl p-8">
                <div className="text-center mb-8">
                    <h1 className="text-4xl font-bold bg-gradient-to-r from-indigo-600 to-purple-600 bg-clip-text text-transparent mb-2">
                        LinkForge
                    </h1>
                    <p className="text-gray-600">Transform documentation into searchable knowledge</p>
                </div>

                <div className="flex flex-col gap-4 mb-8">
                    <input
                        type="url"
                        required
                        placeholder="Enter any documentation URL..."
                        value={url}
                        onChange={(e) => setUrl(e.target.value)}
                        className="p-4 border-2 border-gray-200 rounded-xl focus:ring-2 focus:ring-indigo-400 focus:border-indigo-400 outline-none transition-all text-lg"
                    />
                    <button
                        onClick={handleSubmit}
                        disabled={loading || !url || jobId}
                        className="bg-gradient-to-r from-indigo-600 to-purple-600 text-white py-4 rounded-xl hover:from-indigo-700 hover:to-purple-700 transition-all disabled:opacity-50 disabled:cursor-not-allowed font-semibold text-lg shadow-lg"
                    >
                        {loading ? "Starting..." : jobId ? "Processing..." : "Parse Documentation"}
                    </button>
                </div>

                {error && (
                    <div className="bg-red-50 border-2 border-red-200 rounded-xl p-4 mb-6">
                        <p className="text-red-600 font-semibold flex items-center gap-2">
                            <span className="text-2xl">❌</span>
                            {error}
                        </p>
                    </div>
                )}

                {jobStatus && (
                    <div className="bg-gradient-to-br from-blue-50 to-indigo-50 border-2 border-indigo-200 rounded-2xl p-6 shadow-lg">
                        <div className="flex items-center justify-between mb-6">
                            <div className="flex items-center gap-3">
                                <span className="text-4xl animate-pulse">{getStatusIcon()}</span>
                                <div>
                                    <p className="text-xl font-bold text-indigo-900">
                                        {jobStatus.status === 'completed' ? 'Complete!' :
                                            jobStatus.status === 'failed' ? 'Failed' :
                                                'Processing'}
                                    </p>
                                    <p className="text-sm text-indigo-600">{jobStatus.collection_name}</p>
                                </div>
                            </div>
                            <span className={`px-4 py-2 rounded-full text-sm font-bold shadow-md ${jobStatus.status === 'completed' ? 'bg-green-500 text-white' :
                                jobStatus.status === 'failed' ? 'bg-red-500 text-white' :
                                    'bg-yellow-400 text-yellow-900'
                                }`}>
                                {jobStatus.progress}%
                            </span>
                        </div>

                        {jobStatus.status === 'processing' && (
                            <div className="mb-4">
                                <div className="w-full bg-indigo-100 rounded-full h-4 overflow-hidden shadow-inner">
                                    <div
                                        className="bg-gradient-to-r from-indigo-500 to-purple-500 h-4 rounded-full transition-all duration-500 ease-out"
                                        style={{ width: `${jobStatus.progress}%` }}
                                    />
                                </div>
                            </div>
                        )}

                        <div className="space-y-3 bg-white rounded-xl p-4 shadow-sm">
                            <div className="flex items-start gap-3">
                                <span className="text-indigo-600 font-bold text-sm">STATUS:</span>
                                <p className="text-gray-700 flex-1">{jobStatus.message}</p>
                            </div>

                            <div className="flex items-center gap-3">
                                <span className="text-indigo-600 font-bold text-sm">URL:</span>
                                <p className="text-gray-700 text-sm truncate flex-1">{jobStatus.url}</p>
                            </div>

                            {jobStatus.elapsed_time && (
                                <div className="flex items-center gap-3">
                                    <span className="text-indigo-600 font-bold text-sm">TIME:</span>
                                    <p className="text-gray-700">{jobStatus.elapsed_time.toFixed(1)}s</p>
                                </div>
                            )}

                            {jobStatus.status === 'completed' && (
                                <div className="mt-4 pt-4 border-t border-gray-200">
                                    <p className="text-green-600 font-semibold flex items-center gap-2">
                                        <span>🎉</span>
                                        Documentation successfully processed and indexed!
                                    </p>
                                    <p className="text-sm text-gray-600 mt-2">
                                        Collection ready to query: <span className="font-mono bg-gray-100 px-2 py-1 rounded">{jobStatus.collection_name}</span>
                                    </p>
                                    <p className="text-sm text-gray-600 mt-2">
                                        MCP Server for your Agent: <span className="font-mono bg-gray-100 px-2 py-1 rounded">{jobStatus.mcp_server_url}</span>
                                    </p>
                                </div>
                            )}

                            {jobStatus.status === 'failed' && jobStatus.error && (
                                <div className="mt-4 pt-4 border-t border-gray-200">
                                    <p className="text-red-600 font-semibold">Error Details:</p>
                                    <p className="text-sm text-gray-700 mt-1 bg-red-50 p-3 rounded">{jobStatus.error}</p>
                                </div>
                            )}
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
}