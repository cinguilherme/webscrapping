import scrapy


class RedditSpider(scrapy.Spider):
    name = "reddit"
    start_urls = ["https://www.reddit.com/r/cats"]

    def parse(self, response):
        links = response.xpath("//img/@src")
        hmtl = ""
        extensions = [".jpg", ".gif", ".png"]
        for link in links:
            url = link.get()
            if any(extension in url for extension in extensions):
                yield {
                    'url': {url}
                }
