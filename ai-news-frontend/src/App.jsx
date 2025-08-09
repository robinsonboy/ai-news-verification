import { useState } from 'react'
import Header from './components/Header'
import HeroSection from './components/HeroSection'
import NewsGrid from './components/NewsGrid'
import Footer from './components/Footer'
import { fetchNews, fetchStatistics } from './services/api'
import './App.css'

function App() {
  const [isMenuOpen, setIsMenuOpen] = useState(false)
  const [news, setNews] = useState([])
  const [statistics, setStatistics] = useState(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  // 模擬數據加載
  useState(() => {
    const loadData = async () => {
      try {
        const newsData = await fetchNews()
        setNews(newsData.news)
        const statsData = await fetchStatistics()
        setStatistics(statsData.overview)
      } catch (err) {
        setError('Failed to fetch data.')
        console.error(err)
      } finally {
        setLoading(false)
      }
    }
    loadData()
  }, [])

  const handleSearch = (query) => {
    console.log('Searching for:', query)
    // 這裡可以添加實際的搜尋邏輯，例如重新調用 fetchNews
  }

  const handleNewsCardClick = (newsItem) => {
    console.log('News card clicked:', newsItem.title)
    // 這裡可以導航到新聞詳情頁面
  }

  if (loading) {
    return <div className="flex justify-center items-center h-screen text-xl">載入中...</div>
  }

  if (error) {
    return <div className="flex justify-center items-center h-screen text-xl text-red-500">錯誤: {error}</div>
  }

  return (
    <div className="flex flex-col min-h-screen">
      <Header onSearch={handleSearch} onMenuToggle={() => setIsMenuOpen(!isMenuOpen)} isMenuOpen={isMenuOpen} />
      <main className="flex-1">
        <HeroSection statistics={statistics} />
        <NewsGrid news={news} onNewsCardClick={handleNewsCardClick} />
      </main>
      <Footer />
    </div>
  )
}

export default App
