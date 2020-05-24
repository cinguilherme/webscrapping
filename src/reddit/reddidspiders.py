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
                hmtl += """<a href="{url}" 
                height="33%" 
                width="33%"/>
                </a>""".format(url=url)
                with open("frontpage.html", "a") as page:
                    page.write(hmtl)
                    page.close()
