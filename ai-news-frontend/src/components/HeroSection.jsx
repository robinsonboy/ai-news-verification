import { Card, CardContent } from "@/components/ui/card"
import { CheckCircle, XCircle, Clock } from "lucide-react"

const HeroSection = ({ statistics }) => {
  if (!statistics) {
    return null
  }

  const { total_news, verified_news, fake_news, pending_news, verification_rate } = statistics

  return (
    <section className="bg-gradient-to-r from-blue-700 to-blue-900 text-white py-16 shadow-md">
      <div className="container mx-auto px-4 text-center">
        <h2 className="text-4xl font-bold mb-4 animate-fade-in-down">AI 驅動的真實新聞平台</h2>
        <p className="text-xl mb-8 opacity-90 animate-fade-in-up">
          我們利用先進的 AI 技術，為您提供 100% 經過驗證的可靠新聞，打擊假消息。
        </p>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 max-w-4xl mx-auto">
          <Card className="bg-white text-gray-800 shadow-lg animate-scale-in">
            <CardContent className="p-6">
              <CheckCircle className="h-10 w-10 text-green-600 mx-auto mb-3" />
              <h3 className="text-3xl font-bold mb-1">{verified_news.toLocaleString()}</h3>
              <p className="text-sm">已驗證新聞</p>
            </CardContent>
          </Card>

          <Card className="bg-white text-gray-800 shadow-lg animate-scale-in delay-100">
            <CardContent className="p-6">
              <XCircle className="h-10 w-10 text-red-600 mx-auto mb-3" />
              <h3 className="text-3xl font-bold mb-1">{fake_news.toLocaleString()}</h3>
              <p className="text-sm">疑似假新聞</p>
            </CardContent>
          </Card>

          <Card className="bg-white text-gray-800 shadow-lg animate-scale-in delay-200">
            <CardContent className="p-6">
              <Clock className="h-10 w-10 text-orange-600 mx-auto mb-3" />
              <h3 className="text-3xl font-bold mb-1">{pending_news.toLocaleString()}</h3>
              <p className="text-sm">待驗證新聞</p>
            </CardContent>
          </Card>
        </div>

        <p className="text-2xl font-semibold mt-8 opacity-90 animate-fade-in-up delay-300">
          總計 {total_news.toLocaleString()} 則新聞已分析，驗證率達 <span className="text-yellow-300">{verification_rate}%</span>
        </p>
      </div>
    </section>
  )
}

export default HeroSection

