const results = {
  subject: "Re: New pricing for existing customers",
  sender: "joearmstrong@example.com",
  status: "Open",
  items: [
    {
      id: 1,
      author: "Joe Armstrong",
      date: "Yesterday at 7:24am",
      datetime: "2021-01-28T19:24",
      body: "<p>Thanks so much! Can't wait to try it out.</p>",
    },
    {
      id: 2,
      author: "Monica White",
      date: "Wednesday at 4:35pm",
      datetime: "2021-01-27T16:35",
      body: `
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Malesuada at ultricies tincidunt elit et, enim. Habitant nunc, adipiscing non fermentum, sed est a, aliquet. Lorem in vel libero vel augue aliquet dui commodo.</p>
          <p>Nec malesuada sed sit ut aliquet. Cras ac pharetra, sapien purus vitae vestibulum auctor faucibus ullamcorper. Leo quam tincidunt porttitor neque, velit sed. Tortor mauris ornare ut tellus sed aliquet amet venenatis condimentum. Convallis accumsan et nunc eleifend.</p>
          <p><strong style="font-weight: 600;">Monica White</strong><br/>Customer Service</p>
        `,
    },
    {
      id: 3,
      author: "Joe Armstrong",
      date: "Wednesday at 4:09pm",
      datetime: "2021-01-27T16:09",
      body: `
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Malesuada at ultricies tincidunt elit et, enim. Habitant nunc, adipiscing non fermentum, sed est a, aliquet. Lorem in vel libero vel augue aliquet dui commodo.</p>
          <p>Nec malesuada sed sit ut aliquet. Cras ac pharetra, sapien purus vitae vestibulum auctor faucibus ullamcorper. Leo quam tincidunt porttitor neque, velit sed. Tortor mauris ornare ut tellus sed aliquet amet venenatis condimentum. Convallis accumsan et nunc eleifend.</p>
          <p>– Joe</p>
        `,
    },
  ],
};

import { HomeIcon } from "@heroicons/react/20/solid";

const pages = [
  { name: "Projects", href: "#", current: false },
  { name: "Project Nero", href: "#", current: true },
];

export default function Results() {
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
              <a href="#" className="text-gray-400 hover:text-gray-500">
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

      <ul role="list" className="space-y-2 py-4 sm:space-y-4 sm:px-6 lg:px-8">
        {results.items.map((item) => (
          <li
            key={item.id}
            className="bg-white px-4 py-6 shadow sm:rounded-lg sm:px-6"
          >
            <div className="sm:flex sm:items-baseline sm:justify-between">
              <h3 className="text-base font-medium">
                <span className="text-gray-900">{item.author}</span>{" "}
                <span className="text-gray-600">wrote</span>
              </h3>
              <p className="mt-1 whitespace-nowrap text-sm text-gray-600 sm:mt-0 sm:ml-3">
                <time dateTime={item.datetime}>{item.date}</time>
              </p>
            </div>
            <div
              className="mt-4 space-y-6 text-sm text-gray-800"
              dangerouslySetInnerHTML={{ __html: item.body }}
            />
          </li>
        ))}
      </ul>
    </>
  );
}
