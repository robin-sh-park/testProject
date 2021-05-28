import scrapy

class ScrapingSpider(scrapy.Spider):
    name = 'subject'
    start_urls = [
        'https://gall.dcinside.com/mgallery/board/lists/?id=entj'
    ]

    def parse(self, response):
        for a in response.css('tr.ub-content'):
            href = a.css('a.reply_numbox::attr(href)').extract_first()
            text = a.css('a::text').extract_first()
            href2 = response.urljoin(href)
            yield{
                'text': text,
                'url': href2
            }
# testing successful!
# this file extracts 게시물 제목 and URL
# based on quotes_spider.py
