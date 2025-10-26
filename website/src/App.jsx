import React, { useState } from "react";
import { motion } from "framer-motion";

export default function App() {
    const [url, setUrl] = useState("");
    const [response, setResponse] = useState(null);
    const [loading, setLoading] = useState(false);

    // default max_urls
    const MAX_URLS = 100;

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        setResponse(null);

        try {
            // call your MCP server's endpoint
            const res = await fetch("http://localhost:8000/mcp", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    tool: "process_documentation_url",
                    arguments: {
                        url,               // URL of the documentation
                        max_urls: MAX_URLS,
                        collection_name: url // Use URL itself as collection name
                    },
                }),
            });

            const data = await res.json();

            setResponse({
                domain: "your-mcp-server.com",
                result: data,
                tools: [
                    {
                        name: "list_collections",
                        description:
                            "List all documentation collections available in the MCP server database.",
                        example: "“List all available documentation collections.”",
                    },
                    {
                        name: "query_collections",
                        description:
                            "Query documentation collections to find relevant information.",
                        example:
                            "“Search the API documentation for how to authenticate requests.”",
                    },
                ],
            });
        } catch (err) {
            console.error(err);
            setResponse({ error: "Failed to reach MCP server." });
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

                                <p className="text-gray-700">
                                    Available tools you can query:
                                </p>
                                <ul className="space-y-4">
                                    {response.tools.map((tool, idx) => (
                                        <li key={idx} className="bg-white rounded-lg shadow p-4">
                                            <p className="font-semibold text-indigo-700">
                                                {tool.name}
                                            </p>
                                            <p className="text-gray-600">{tool.description}</p>
                                            <p className="text-sm text-gray-500 mt-2">
                                                Example: <em>{tool.example}</em>
                                            </p>
                                        </li>
                                    ))}
                                </ul>

                                <div className="mt-6 bg-white rounded-lg p-4 shadow">
                                    <p className="font-semibold text-indigo-700 mb-2">
                                        Tool response:
                                    </p>
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
