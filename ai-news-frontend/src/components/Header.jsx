import { useState } from 'react'
import { Search, Menu, X, Bot } from 'lucide-react'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'

const Header = ({ onSearch, onMenuToggle, isMenuOpen }) => {
  const [searchQuery, setSearchQuery] = useState('')

  const handleSearch = (e) => {
    e.preventDefault()
    if (onSearch) {
      onSearch(searchQuery)
    }
  }

  return (
    <header className="bg-blue-900 text-white shadow-lg">
      <div className="container mx-auto px-4">
        <div className="flex items-center justify-between h-16">
          {/* Logo 和網站名稱 */}
          <div className="flex items-center space-x-3">
            <Bot className="h-8 w-8 text-blue-300" />
            <div>
              <h1 className="text-xl font-bold">AI 新聞驗證</h1>
              <p className="text-xs text-blue-300">100% 可信新聞</p>
            </div>
          </div>

          {/* 桌面版導航 */}
          <nav className="hidden md:flex items-center space-x-6">
            <a href="/" className="hover:text-blue-300 transition-colors">首頁</a>
            <a href="/categories" className="hover:text-blue-300 transition-colors">分類</a>
            <a href="/submit" className="hover:text-blue-300 transition-colors">提交驗證</a>
            <a href="/statistics" className="hover:text-blue-300 transition-colors">統計</a>
            <a href="/about" className="hover:text-blue-300 transition-colors">關於</a>
          </nav>

          {/* 搜尋框 */}
          <form onSubmit={handleSearch} className="hidden md:flex items-center space-x-2">
            <div className="relative">
              <Input
                type="text"
                placeholder="搜尋新聞..."
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                className="w-64 bg-white text-gray-900 border-0"
              />
              <Button
                type="submit"
                size="sm"
                className="absolute right-1 top-1 h-7 w-7 p-0 bg-blue-600 hover:bg-blue-700"
              >
                <Search className="h-4 w-4" />
              </Button>
            </div>
          </form>

          {/* 手機版選單按鈕 */}
          <Button
            variant="ghost"
            size="sm"
            className="md:hidden text-white hover:bg-blue-800"
            onClick={onMenuToggle}
          >
            {isMenuOpen ? <X className="h-6 w-6" /> : <Menu className="h-6 w-6" />}
          </Button>
        </div>

        {/* 手機版選單 */}
        {isMenuOpen && (
          <div className="md:hidden border-t border-blue-800 py-4">
            <nav className="flex flex-col space-y-3">
              <a href="/" className="hover:text-blue-300 transition-colors">首頁</a>
              <a href="/categories" className="hover:text-blue-300 transition-colors">分類</a>
              <a href="/submit" className="hover:text-blue-300 transition-colors">提交驗證</a>
              <a href="/statistics" className="hover:text-blue-300 transition-colors">統計</a>
              <a href="/about" className="hover:text-blue-300 transition-colors">關於</a>
            </nav>
            
            {/* 手機版搜尋 */}
            <form onSubmit={handleSearch} className="mt-4">
              <div className="flex space-x-2">
                <Input
                  type="text"
                  placeholder="搜尋新聞..."
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)}
                  className="flex-1 bg-white text-gray-900"
                />
                <Button type="submit" size="sm" className="bg-blue-600 hover:bg-blue-700">
                  <Search className="h-4 w-4" />
                </Button>
              </div>
            </form>
          </div>
        )}
      </div>
    </header>
  )
}

export default Header

