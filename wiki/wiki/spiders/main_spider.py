# https://letslearnabout.net/python/scrapy/scrapy-setting-up-our-first-spider/
# https://letslearnabout.net/python/scrapy/scrapy-visiting-next-pages/
# -*- coding: utf-8 -*-
import scrapy


class MainSpiderSpider(scrapy.Spider):
    name = 'main_spider'
    # name has to be unique; identifies spider
    allowed_domains = ['quotes.toscrape.com']
    # requests outside allowed_domains won't be followed
    start_urls = ['http://quotes.toscrape.com']
    # where our spider will start scraping

    def parse(self, response):
        # default callback. scrapy will launch this method first to process the response(returning data)
        quotes = response.xpath('//div[@class="quote"]')

        for quote in quotes:
            text = quote.xpath('./span[@class="text"]/text()').extract_first()
            author = quotes.xpath('.//small[@class="author"]/text()').extract_first()
            tags = quotes.xpath('.//div[@class="tags"]/a/text()').extract()

            yield {
                'Quote': text,
                'Author': author,
                'Tags': tags
            }

        next_page_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_page_url:  # if next_page_url exists...
            next_page_absolute_url = response.urljoin(next_page_url)
            yield scrapy.Request(next_page_absolute_url, self.parse)
