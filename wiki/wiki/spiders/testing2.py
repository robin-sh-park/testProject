import scrapy

class testingSpider(scrapy.Spider):
    name = 'test2'
    start_urls = [
        'https://gall.dcinside.com/mgallery/board/lists/?id=entj'
    ]

    def parse(self, response):
        tr = response.xpath('//tr[@class="ub-content us-post"]')  # 5?

        # give the extracted content row wise
        for item in tr:
            title = item.xpath('./td[@class="gall_tit ub-word"]/a/text()').extract_first()
            url = item.xpath('./td[@class="gall_tit ub-word"]/a/@href').extract_first()
            # text = item.xpath('./a/text()').extract()

            # yield or give the scraped info to scrapy
            yield {
                title,
                url,
                # text
            }
