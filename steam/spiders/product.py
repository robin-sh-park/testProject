import scrapy

class ProductSpider(scrapy.Spider):
    name = 'products'
    start_urls = [
        'https://store.steampowered.com/search/?sort_by=Released_DESC'
    ]
    allowed_domains = ["steampowered.com"]
    rules = [
        Rule(LinkExtractor(
            allow='/app/(.+)/',
            restrict_css='#search_result_container'),
            callback='parse_product'),
        Rule(LinkExtractor(
                allow='page=(d+)',
                restrict_css='.search_pagination_right')),
    ]

    def parse_product(self, response):
        return {
            'app_name': response.css('.apphub_AppName::text').extract_first(),
            'specs': response.css('.game_area_details specs a:: text').extract()
        }

class ProductItem(scrapy.Item):
    app_name = scrapy.Field()
    specs = scrapy.Field()
    n_reviews = scrapy.Field()

    product = ProductItem()
