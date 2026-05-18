"use client";

import axios from "axios";
import { useState } from "react";

export default function Home() {

  const [query, setQuery] = useState("");
  const [loading, setLoading] = useState(false);

  const [result, setResult] = useState<any>(null);

  async function analyzeQuery() {

    if (!query) return;

    setLoading(true);

    try {

      const response = await axios.post(
        "https://pharmasense-37128349600.asia-south1.run.app/analyze",
        {
          query: query
        }
      );

      setResult(response.data);

    } catch (error) {

      console.error(error);

    }

    setLoading(false);
  }

  return (

    <main className="min-h-screen bg-black text-white p-10">

      <h1 className="text-5xl font-bold">
        PharmaSense
      </h1>

      <p className="mt-4 text-zinc-400">
        Multi-Agent Biomedical Research System
      </p>

      <div className="mt-10 flex gap-4">

        <input
          type="text"
          placeholder="Analyze aspirin for neuroinflammation..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          className="w-full rounded-xl bg-zinc-900 border border-zinc-700 p-4"
        />

        <button
          onClick={analyzeQuery}
          className="bg-white text-black px-6 rounded-xl font-semibold"
        >
          {loading ? "Analyzing..." : "Analyze"}
        </button>

      </div>

      {result && (

        <div className="mt-10 space-y-6">

          {/* Metrics Card */}
          <div className="bg-zinc-900 p-6 rounded-2xl">

            <h2 className="text-2xl font-semibold mb-4">
              System Metrics
            </h2>

            <div className="space-y-3 text-zinc-300">

              <p>
                Retrieved Papers:
                {" "}
                {result.retrieved_docs.length}
              </p>

              <p>
                Literature Agent Time:
                {" "}
                {result.metrics?.literature_agent_time?.toFixed(2)}s
              </p>

              <p>
                Mechanism Agent Time:
                {" "}
                {result.metrics?.mechanism_agent_time?.toFixed(2)}s
              </p>

              <p>
                Total Pipeline Time:
                {" "}
                {result.metrics?.total_pipeline_time?.toFixed(2)}s
              </p>

            </div>

          </div>


          {/* Literature Analysis */}
          <div className="bg-zinc-900 p-6 rounded-2xl">

            <h2 className="text-2xl font-semibold mb-4">
              Literature Analysis
            </h2>

            <p className="text-zinc-300 whitespace-pre-wrap">
              {result.literature_analysis.summary}
            </p>

          </div>


          {/* Mechanism Analysis */}
          <div className="bg-zinc-900 p-6 rounded-2xl">

            <h2 className="text-2xl font-semibold mb-4">
              Mechanism Analysis
            </h2>

            <p className="text-zinc-300 whitespace-pre-wrap">
              {result.mechanism_analysis.summary}
            </p>

          </div>


          {/* Retrieved Papers */}
          <div className="bg-zinc-900 p-6 rounded-2xl">

            <h2 className="text-2xl font-semibold mb-4">
              Retrieved Papers
            </h2>

            <div className="space-y-4">

              {result.retrieved_docs.map(
                (doc: any, index: number) => (

                  <div
                    key={index}
                    className="border border-zinc-700 rounded-xl p-4"
                  >

                    <h3 className="font-semibold">
                      {doc.title}
                    </h3>

                    <p className="text-zinc-400 mt-2">
                      {doc.abstract}
                    </p>

                  </div>

                )
              )}

            </div>

          </div>

        </div>

      )}

    </main>

  );
}