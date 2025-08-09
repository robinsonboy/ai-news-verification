import NewsCard from "./NewsCard"

const NewsGrid = ({ news, onNewsCardClick }) => {
  return (
    <section className="py-8">
      <div className="container mx-auto px-4">
        <h2 className="text-3xl font-bold text-center mb-8 text-gray-800">最新新聞</h2>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
          {news.map((item) => (
            <NewsCard key={item.id} news={item} onClick={onNewsCardClick} />
          ))}
        </div>
      </div>
    </section>
  )
}

export default NewsGrid

