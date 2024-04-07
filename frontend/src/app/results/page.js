"use client";

import { useState, useEffect, useCallback } from "react";
import { useSearchParams } from "next/navigation";

import SearchInput from "../components/SearchInput";
import SearchButton from "../components/SearchButton";
import { HomeIcon } from "@heroicons/react/20/solid";
import { useRouter } from "next/navigation";

const pages = [{ name: "Results", href: "#", current: true }];

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
    } else {
      router.push("/");
    }
  }, [query, router]);

  return (
    <>
      <nav
        className="flex border-b border-gray-200 bg-white"
        aria-label="Breadcrumb"
      >
        <ol
          role="list"
          className="mx-auto flex w-full max-w-screen-xl space-x-4 px-4 sm:px-6 lg:px-8"
        >
          <li className="flex">
            <div className="flex items-center">
              <a href="/" className="text-gray-400 hover:text-gray-500">
                <HomeIcon
                  className="h-5 w-5 flex-shrink-0"
                  aria-hidden="true"
                />
                <span className="sr-only">Home</span>
              </a>
            </div>
          </li>
          {pages.map((page) => (
            <li key={page.name} className="flex">
              <div className="flex items-center">
                <svg
                  className="h-full w-6 flex-shrink-0 text-gray-200"
                  viewBox="0 0 24 44"
                  preserveAspectRatio="none"
                  fill="currentColor"
                  xmlns="http://www.w3.org/2000/svg"
                  aria-hidden="true"
                >
                  <path d="M.293 0l22 22-22 22h1.414l22-22-22-22H.293z" />
                </svg>
                <a
                  href={page.href}
                  className="ml-4 text-sm font-medium text-gray-500 hover:text-gray-700"
                  aria-current={page.current ? "page" : undefined}
                >
                  {page.name}
                </a>
              </div>
            </li>
          ))}
        </ol>
      </nav>
      <div className="flex flex-row">
        <SearchInput
          setSearchQuery={setSearchQuery}
          className={
            " flex rounded-xl border-gray-300 px-4 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-lg"
          }
        />
        <SearchButton
          goToResults={goToResults}
          searchQuery={searchQuery}
          className={
            "mt-8 inline-flex rounded-md border border-transparent bg-indigo-600 px-6 py-3 text-base font-medium text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
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
                  <span className="text-gray-900">{item.assigned_to}</span>{" "}
                  <span className="text-gray-600">wrote</span>
                </h3>
                <p className="mt-1 whitespace-nowrap text-sm text-gray-600 sm:mt-0 sm:ml-3">
                  <time dateTime={item.datetime}>{item.date_filed}</time>
                </p>
              </div>
              <div className="mt-4 space-y-6 text-sm text-gray-800">
                {item.text}
              </div>
              {/* <div
              className="mt-4 space-y-6 text-sm text-gray-800"
              dangerouslySetInnerHTML={{ __html: item.body }}
            /> */}
            </li>
          ))}
      </ul>
    </>
  );
}
