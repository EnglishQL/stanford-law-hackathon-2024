"use client";

export default function Home() {
  return (
    <div className="relative overflow-hidden bg-gray-50">
      <div className="relative pt-6 pb-16 sm:pb-24">
        <main className="mx-auto mt-16 max-w-7xl px-4 sm:mt-24">
          <div className="text-center">
            <h1 className="text-4xl font-bold tracking-tight text-gray-900 sm:text-5xl md:text-6xl">
              <span className="block xl:inline">Powerful semantic search</span>{" "}
              <span className="block text-indigo-600 xl:inline">for PACER</span>
            </h1>
            <p className="mx-auto mt-3 max-w-md text-base text-gray-500 sm:text-lg md:mt-5 md:max-w-3xl md:text-xl">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do
            </p>

            <div className="mx-auto mt-5 max-w-md sm:flex sm:justify-center md:mt-8">
              <input
                type="text"
                name="name"
                id="name"
                className=" w-full flex justify-center rounded-full border-gray-300 px-4 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-lg"
                placeholder="Tell me what you're looking for..."
              />
            </div>
            <button
              type="button"
              className="mt-8 inline-flex items-center rounded-md border border-transparent bg-indigo-600 px-6 py-3 text-base font-medium text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
            >
              Search
            </button>
          </div>
        </main>
      </div>
    </div>
  );
}
