import React, { useState } from "react";

export default function App() {
    const [url, setUrl] = useState("");
    const [response, setResponse] = useState(null);
    const [loading, setLoading] = useState(false);

    const MAX_URLS = 2;

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        setResponse(null);

        try {
            const res = await fetch("http://localhost:8000/api/process", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    url: url,
                    max_urls: MAX_URLS,
                    collection_name: url
                }),
            });

            if (!res.ok) {
                const text = await res.text();
                throw new Error(`${res.status} ${res.statusText}: ${text}`);
            }

            const data = await res.json();

            setResponse({
                domain: "localhost:8000",
                result: data,
            });
        } catch (err) {
            console.error('Error details:', err);
            setResponse({
                error: err.message || 'Unknown error occurred'
            });
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="min-h-screen flex flex-col items-center justify-center bg-gradient-to-br from-indigo-50 to-white p-6">
            <div className="w-full max-w-lg bg-white rounded-2xl shadow-xl p-8">
                <h1 className="text-3xl font-bold text-indigo-600 mb-6 text-center">
                    LinkForge
                </h1>

                <div className="flex flex-col gap-4">
                    <input
                        type="url"
                        required
                        placeholder="Enter any documentation URL..."
                        value={url}
                        onChange={(e) => setUrl(e.target.value)}
                        className="p-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-indigo-400 outline-none"
                    />
                    <button
                        onClick={handleSubmit}
                        disabled={loading || !url}
                        className="bg-indigo-600 text-white py-3 rounded-xl hover:bg-indigo-700 transition-all disabled:opacity-50 disabled:cursor-not-allowed"
                    >
                        {loading ? "Processing..." : "Parse my Documentation!"}
                    </button>
                </div>

                {response && (
                    <div className="mt-8 bg-indigo-50 rounded-xl p-5 space-y-4">
                        {response.error ? (
                            <p className="text-red-600 font-semibold">{response.error}</p>
                        ) : (
                            <>
                                <h2 className="text-xl font-semibold text-indigo-700 mb-2">
                                    Connected to: {response.domain}
                                </h2>

                                <div className="bg-white rounded-lg p-4 shadow">
                                    <p className="font-semibold text-indigo-700 mb-2">Tool response:</p>
                                    <pre className="text-sm text-gray-700 whitespace-pre-wrap break-words">
                                        {JSON.stringify(response.result, null, 2)}
                                    </pre>
                                </div>
                            </>
                        )}
                    </div>
                )}
            </div>
        </div>
    );
}