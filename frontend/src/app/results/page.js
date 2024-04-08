"use client";

import { useState, useEffect, useCallback } from "react";
import { useSearchParams } from "next/navigation";

import SearchInput from "../components/SearchInput";
import SearchButton from "../components/SearchButton";
import { useRouter } from "next/navigation";

export default function Results() {
  const [results, setResults] = useState(null); // [ { title: "Title", content: "Content" }

  const [searchQuery, setSearchQuery] = useState("");
  const searchParams = useSearchParams();

  const router = useRouter();
  const query = searchParams.get("query");

  const goToResults = (query) => {
    const queryParam = encodeURIComponent(query);
    console.log(`Searching for ${query}`);
    router.push(`/results?query=${queryParam}`);
  };

  const search = useCallback(
    async (query) => {
      const response = await fetch("http://localhost:8000/api/search", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ query }),
      });
      setResults(await response.json());
    },
    [setResults]
  );

  useEffect(() => {
    if (query) {
      search(query);
      setSearchQuery(query);
    } else {
      router.push("/");
    }
  }, [query, router]);

  return (
    <>
      <div className="mt-8 mx-8 flex flex-row items-center space-x-4">
        <SearchInput
          setSearchQuery={setSearchQuery}
          value={searchQuery}
          className={
            "flex-grow rounded-xl border-gray-300 px-4 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-lg"
          }
        />
        <SearchButton
          goToResults={goToResults}
          searchQuery={searchQuery}
          className={
            "flex-shrink-0 rounded-md border border-transparent bg-indigo-600 px-6 py-3 text-base font-medium text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
          }
        />
      </div>
      <ul role="list" className="space-y-2 py-4 sm:space-y-4 sm:px-6 lg:px-8">
        {results &&
          results.length > 0 &&
          results.map((item) => (
            <li
              key={item.id}
              className="bg-white px-4 py-6 shadow sm:rounded-lg sm:px-6"
            >
              <div className="sm:flex sm:items-baseline sm:justify-between">
                <h3 className="text-base font-medium">
                  <span className="text-gray-900">{item.case_name}</span>{" "}
                  <span className="text-gray-600">wrote</span>
                </h3>
                <p className="mt-1 whitespace-nowrap text-sm text-gray-600 sm:mt-0 sm:ml-3">
                  <time dateTime={item.datetime}>{item.date_filed}</time>
                </p>
              </div>
              {/* <div className="mt-4 space-y-6 text-sm text-gray-800">
                {item.text}
              </div> */}
              <div
                className="mt-8"
                style={{ maxHeight: "7em", overflowY: "auto" }}
              >
                <pre>{item.text}</pre>
              </div>
            </li>
          ))}
      </ul>
    </>
  );
}
