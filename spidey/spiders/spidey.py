import scrapy

class Spidey(scrapy.Spider):
    name = "spidey"
    
    def start_requests(self):
        urls = {
                'https://www.reddit.com',
                'https://www.reddit.com/r/gaming',
                'https://www.reddit.com/r/conspiracy'
                }
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        #only concerned with following links for now
        next_page = response.css('link::attr(href)').extract_first()
        if (next_page is not None):
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
