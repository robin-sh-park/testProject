import scrapy

class ScrapingSpider(scrapy.Spider):
    name = 'mbti'
    start_urls = [  # is this too much????? maybe mixed bag will be too confusing
        'https://gall.dcinside.com/mgallery/board/lists/?id=entj',
        'https://gall.dcinside.com/mgallery/board/lists/?id=estp',
        'https://gall.dcinside.com/mgallery/board/lists/?id=intp',
        'https://gall.dcinside.com/mgallery/board/lists/?id=istp'
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
