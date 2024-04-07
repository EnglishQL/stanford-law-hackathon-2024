export default function SearchInput({ setSearchQuery, className, value }) {
  return (
    <textarea
      name="name"
      id="name"
      className={className}
      rows="0"
      placeholder="Tell me what you're looking for..."
      style={{ resize: "none" }}
      value={value}
      onInput={(e) => {
        setSearchQuery(e.target.value);
        e.target.style.height = "inherit";
        e.target.style.height = `${Math.min(e.target.scrollHeight, 10 * 18)}px`; // 18 is an estimated line height
      }}
    ></textarea>
  );
}
