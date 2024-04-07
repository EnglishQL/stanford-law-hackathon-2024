export default function SearchButton({ searchQuery, goToResults, className }) {
  return (
    <button
      type="button"
      onClick={() => {
        goToResults(searchQuery);
      }}
      className={className}
    >
      Search
    </button>
  );
}
