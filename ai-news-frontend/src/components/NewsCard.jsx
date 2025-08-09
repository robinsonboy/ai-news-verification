import { CheckCircle, AlertCircle, XCircle, Clock, ExternalLink } from 'lucide-react'
import { Card, CardContent, CardHeader } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { Button } from '@/components/ui/button'

const NewsCard = ({ news, onClick }) => {
  const getVerificationIcon = (status) => {
    switch (status) {
      case 'verified':
        return <CheckCircle className="h-5 w-5 text-green-600" />
      case 'fake':
        return <XCircle className="h-5 w-5 text-red-600" />
      case 'reviewing':
      case 'questionable':
        return <AlertCircle className="h-5 w-5 text-orange-600" />
      default:
        return <Clock className="h-5 w-5 text-gray-600" />
    }
  }

  const getVerificationText = (status) => {
    switch (status) {
      case 'verified':
        return '已驗證'
      case 'fake':
        return '疑似假新聞'
      case 'reviewing':
        return '審核中'
      case 'questionable':
        return '可疑'
      default:
        return '待驗證'
    }
  }

  const getVerificationColor = (status) => {
    switch (status) {
      case 'verified':
        return 'bg-green-100 text-green-800 border-green-200'
      case 'fake':
        return 'bg-red-100 text-red-800 border-red-200'
      case 'reviewing':
      case 'questionable':
        return 'bg-orange-100 text-orange-800 border-orange-200'
      default:
        return 'bg-gray-100 text-gray-800 border-gray-200'
    }
  }

  const getScoreColor = (score) => {
    if (score >= 80) return 'text-green-600'
    if (score >= 60) return 'text-orange-600'
    return 'text-red-600'
  }

  const formatDate = (dateString) => {
    if (!dateString) return ''
    const date = new Date(dateString)
    return date.toLocaleDateString('zh-TW', {
      year: 'numeric',
      month: 'short',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    })
  }

  return (
    <Card className="hover:shadow-lg transition-shadow cursor-pointer" onClick={() => onClick && onClick(news)}>
      <CardHeader className="pb-3">
        <div className="flex items-start justify-between gap-3">
          <h3 className="font-semibold text-lg leading-tight line-clamp-2 flex-1">
            {news.title}
          </h3>
          <div className="flex items-center gap-2 flex-shrink-0">
            {getVerificationIcon(news.verification_status)}
            {news.credibility_score !== null && (
              <span className={`font-bold text-lg ${getScoreColor(news.credibility_score)}`}>
                {Math.round(news.credibility_score)}
              </span>
            )}
          </div>
        </div>
        
        <div className="flex items-center gap-2 mt-2">
          <Badge className={getVerificationColor(news.verification_status)}>
            {getVerificationText(news.verification_status)}
          </Badge>
          <Badge variant="outline" className="text-xs">
            {news.category}
          </Badge>
        </div>
      </CardHeader>

      <CardContent>
        <p className="text-gray-600 text-sm line-clamp-3 mb-3">
          {news.content.substring(0, 150)}...
        </p>
        
        <div className="flex items-center justify-between text-xs text-gray-500">
          <div className="flex items-center gap-2">
            <span className="font-medium">{news.source}</span>
            {news.published_at && (
              <>
                <span>•</span>
                <span>{formatDate(news.published_at)}</span>
              </>
            )}
          </div>
          
          {news.url && (
            <Button
              variant="ghost"
              size="sm"
              className="h-6 px-2 text-xs"
              onClick={(e) => {
                e.stopPropagation()
                window.open(news.url, '_blank')
              }}
            >
              <ExternalLink className="h-3 w-3 mr-1" />
              原文
            </Button>
          )}
        </div>
      </CardContent>
    </Card>
  )
}

export default NewsCard

