# https://www.analyticsvidhya.com/blog/2017/07/web-scraping-in-python-using-scrapy/
import scrapy


class RedditbotSpider(scrapy.Spider):
    # spider name
    name = 'redditbot'
    # list of allowed domains
    allowed_domains = ['www.reddit.com/r/gameofthrones/']  # 'http://www.reddit.com/r/gameofthrones/'
    # starting url for scraping
    start_urls = ['https://www.reddit.com/r/gameofthrones/']  # http://http://www.reddit.com/r/gameofthrones//
    # location of csv file
    custom_settings = {  # custom_settings
        # 'FEED_URI': 'tmp/reddit.csv'
        'FEEDS': {
            'reddit.csv': {
                'format': 'csv',
                'fields': ['titles', 'votes', 'times', 'comments'],
            },
        },
    }

    def parse(self, response):
        # extracting the content using css selectors
        titles = response.css('.title.may-blank::text').extract()
        votes = response.css('.score.unvoted::text').extract()
        times = response.css('time::attr(title)').extract()
        comments = response.css('.comments::text').extract()

        # give the extracted content row wise
        for item in zip(titles, votes, times, comments):
            # create a dictionary to store the scraped info
            scraped_info = {
                'title': item[0],
                'vote': item[1],
                'created_at': item[2],
                'comments': item[3],
            }

            # yield or give the scraped info to scrapy
            yield scraped_info
