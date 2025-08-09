import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from datetime import datetime

class NewsCrawlerService:
    def fetch_and_parse(self, url):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status() # 檢查 HTTP 錯誤
            soup = BeautifulSoup(response.text, 'html.parser')

            title = self._extract_title(soup)
            content = self._extract_content(soup)
            source = self._extract_source(url)
            published_at = self._extract_published_at(soup)

            return {
                "title": title,
                "content": content,
                "source": source,
                "published_at": published_at,
                "url": url
            }
        except requests.exceptions.RequestException as e:
            print(f"爬取或解析失敗: {e}")
            return None

    def _extract_title(self, soup):
        # 嘗試從常見的標籤中提取標題
        title_tags = ["h1", "title", "meta[property=\"og:title\"]", "meta[name=\"twitter:title\"]"]
        for tag in title_tags:
            element = soup.select_one(tag)
            if element:
                if tag.startswith("meta"):
                    return element.get("content")
                return element.get_text(strip=True)
        return "無標題"

    def _extract_content(self, soup):
        # 嘗試從常見的內容標籤中提取內容
        content_tags = ["article", "div.content", "div.article-body", "div.entry-content", "div.post-content"]
        for tag in content_tags:
            element = soup.select_one(tag)
            if element:
                paragraphs = element.find_all(["p", "h1", "h2", "h3", "h4", "h5", "h6", "li"])
                return "\n".join([p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)])
        return "無內容"

    def _extract_source(self, url):
        parsed_url = urlparse(url)
        return parsed_url.netloc.replace("www.", "")

    def _extract_published_at(self, soup):
        # 嘗試從常見的日期時間標籤中提取發布時間
        date_tags = ["time", "meta[property=\"article:published_time\"]", "meta[name=\"pubdate\"]"]
        for tag in date_tags:
            element = soup.select_one(tag)
            if element:
                if tag.startswith("meta"):
                    date_str = element.get("content")
                else:
                    date_str = element.get("datetime") or element.get_text(strip=True)
                
                try:
                    # 嘗試解析多種日期格式
                    from dateutil.parser import parse
                    return parse(date_str)
                except Exception:
                    pass
        return None


