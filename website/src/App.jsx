import React, { useState } from "react";
import { motion } from "framer-motion";

export default function App() {
    const [url, setUrl] = useState("");
    const [response, setResponse] = useState(null);
    const [loading, setLoading] = useState(false);

    // default max_urls
    const MAX_URLS = 2;

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        setResponse(null);

        try {
            // FastMCP with streamable-http expects SSE format
            const savedSessionId = localStorage.getItem("mcp_session_id");

            const res = await fetch("/mcp", {
                method: "POST",
                headers: {
                    "Accept": "application/json, text/event-stream",
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    jsonrpc: "2.0",
                    method: "tools/call",
                    params: {
                        name: "process_documentation_url",
                        arguments: {
                            url: url,
                            max_urls: MAX_URLS,
                            collection_name: url
                        }
                    },
                    id: Date.now()
                }),
                credentials: "include"
            });

            const newSession = res.headers.get("x-session-id");
            if (newSession) {
                localStorage.setItem("mcp_session_id", newSession);
            }

            if (!res.ok) {
                const text = await res.text();
                throw new Error(`${res.status} ${res.statusText}: ${text}`);
            }

            // Read the streaming response
            const reader = res.body.getReader();
            const decoder = new TextDecoder();
            let buffer = '';
            let finalResult = null;

            while (true) {
                const { done, value } = await reader.read();

                if (done) break;

                buffer += decoder.decode(value, { stream: true });

                // Process complete SSE messages
                const lines = buffer.split('\n');
                buffer = lines.pop() || ''; // Keep incomplete line in buffer

                for (const line of lines) {
                    if (line.startsWith('data: ')) {
                        try {
                            const jsonStr = line.slice(6); // Remove 'data: ' prefix
                            const parsed = JSON.parse(jsonStr);

                            // Look for the result in the JSON-RPC response
                            if (parsed.result) {
                                finalResult = parsed.result;
                            }
                        } catch (parseError) {
                            console.warn('Failed to parse SSE data:', line);
                        }
                    }
                }
            }

            // Process any remaining buffer
            if (buffer.startsWith('data: ')) {
                try {
                    const jsonStr = buffer.slice(6);
                    const parsed = JSON.parse(jsonStr);
                    if (parsed.result) {
                        finalResult = parsed.result;
                    }
                } catch (parseError) {
                    console.warn('Failed to parse final buffer:', buffer);
                }
            }

            if (!finalResult) {
                throw new Error('No result received from server');
            }

            setResponse({
                domain: "localhost:8000",
                result: finalResult,
                tools: [
                    {
                        name: "list_collections",
                        description:
                            "List all documentation collections available in the MCP server database.",
                        example: "List all available documentation collections.",
                    },
                    {
                        name: "query_documentation",
                        description:
                            "Query documentation collections to find relevant information.",
                        example:
                            "Search the API documentation for how to authenticate requests.",
                    },
                ],
            });
        } catch (err) {
            console.error('Error details:', err);
            setResponse({
                error: `Failed to reach MCP server: ${err.message}`
            });
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="min-h-screen flex flex-col items-center justify-center bg-gradient-to-br from-indigo-50 to-white p-6">
            <motion.div
                initial={{ opacity: 0, y: -10 }}
                animate={{ opacity: 1, y: 0 }}
                className="w-full max-w-lg bg-white rounded-2xl shadow-xl p-8"
            >
                <h1 className="text-3xl font-bold text-indigo-600 mb-6 text-center">
                    LinkForge
                </h1>

                <form onSubmit={handleSubmit} className="flex flex-col gap-4">
                    <input
                        type="url"
                        required
                        placeholder="Enter any documentation URL..."
                        value={url}
                        onChange={(e) => setUrl(e.target.value)}
                        className="p-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-indigo-400 outline-none"
                    />
                    <button
                        type="submit"
                        disabled={loading}
                        className="bg-indigo-600 text-white py-3 rounded-xl hover:bg-indigo-700 transition-all"
                    >
                        {loading ? "Processing..." : "Parse my Documentation!"}
                    </button>
                </form>

                {response && (
                    <motion.div
                        initial={{ opacity: 0 }}
                        animate={{ opacity: 1 }}
                        className="mt-8 bg-indigo-50 rounded-xl p-5 space-y-4"
                    >
                        {response.error ? (
                            <p className="text-red-600 font-semibold">{response.error}</p>
                        ) : (
                            <>
                                <h2 className="text-xl font-semibold text-indigo-700 mb-2">
                                    Connected to: {response.domain}
                                </h2>

                                <p className="text-gray-700">Available tools you can query:</p>
                                <ul className="space-y-4">
                                    {response.tools.map((tool, idx) => (
                                        <li key={idx} className="bg-white rounded-lg shadow p-4">
                                            <p className="font-semibold text-indigo-700">{tool.name}</p>
                                            <p className="text-gray-600">{tool.description}</p>
                                            <p className="text-sm text-gray-500 mt-2">
                                                Example: <em>{tool.example}</em>
                                            </p>
                                        </li>
                                    ))}
                                </ul>

                                <div className="mt-6 bg-white rounded-lg p-4 shadow">
                                    <p className="font-semibold text-indigo-700 mb-2">Tool response:</p>
                                    <pre className="text-sm text-gray-700 whitespace-pre-wrap break-words">
                                        {JSON.stringify(response.result, null, 2)}
                                    </pre>
                                </div>
                            </>
                        )}
                    </motion.div>
                )}
            </motion.div>
        </div>
    );
}
