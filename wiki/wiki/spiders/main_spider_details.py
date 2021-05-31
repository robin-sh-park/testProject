# https://letslearnabout.net/python/scrapy/scrapy-getting-all-the-details/
import scrapy


class MainDetailSpider(scrapy.Spider):
    name = 'detail_spider'
    # name has to be unique; identifies spider
    allowed_domains = ['quotes.toscrape.com']
    # requests outside allowed_domains won't be followed
    start_urls = ['http://quotes.toscrape.com']
    # where our spider will start scraping

    def parse(self, response):
        quotes = response.xpath('//div[@class="quote"]')

        for quote in quotes:
            author_partial_link = quote.xpath('.//span/a/@href').extract_first()
            author_link = response.urljoin(author_partial_link)

            yield scrapy.Request(author_link, callback=self.parse_author)

        next_page_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_page_url:
            next_page_absolute_url = 'http://quotes.toscrape.com/' + next_page_url
            yield scrapy.Request(next_page_absolute_url, self.parse)

    def parse_author(self, response):
        name = response.xpath('//h3[@class="author-title"]/text()').extract_first().strip()
        born_date = response.xpath('//span[@class="author-born-date"]/text()').extract_first().strip()
        born_location = response.xpath('//span[@class="author-born-location"]/text()').extract_first().strip()[3:]
        description = response.xpath('//div[@class="author-description"]/text()').extract_first().strip()

        yield {
            'name': name,
            'born_date': born_date,
            'born_location': born_location,
            'description': description,
        }
