const Footer = () => {
  return (
    <footer className="bg-gray-800 text-white py-6 mt-auto">
      <div className="container mx-auto px-4 text-center text-sm">
        <p>&copy; {new Date().getFullYear()} AI 新聞驗證. All rights reserved.</p>
        <p className="mt-2">
          <a href="/privacy" className="hover:text-blue-400 transition-colors">隱私政策</a>
          <span className="mx-2">|</span>
          <a href="/terms" className="hover:text-blue-400 transition-colors">使用條款</a>
        </p>
      </div>
    </footer>
  )
}

export default Footer

