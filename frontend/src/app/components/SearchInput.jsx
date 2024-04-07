export default function SearchInput({ setSearchQuery, className }) {
  return (
    <div className="mx-auto mt-5 max-w-md sm:flex sm:justify-center md:mt-8">
      <textarea
        name="name"
        id="name"
        className={className}
        rows="0"
        placeholder="Tell me what you're looking for..."
        style={{ resize: "none" }}
        onInput={(e) => {
          setSearchQuery(e.target.value);
          e.target.style.height = "inherit";
          e.target.style.height = `${Math.min(
            e.target.scrollHeight,
            10 * 18
          )}px`; // 24 is an estimated line height
        }}
      ></textarea>
    </div>
  );
}
