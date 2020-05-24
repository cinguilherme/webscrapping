import bs4
import time
import schedule

import asyncio
from pyppeteer import launch

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

print("playgorund ran successfully")
print("this will keep scraping on a time based")


async def scrapeWithPup():
    browser = await launch(options={'args': ['--no-sandbox']})
    page = await browser.newPage()
    await page.goto('http://www.google.com')
    dimensions = await page.evaluate('''() => {
        return {
            width: document.documentElement.clientWidth,
            height: document.documentElement.clientHeight,
            deviceScaleFactor: window.devicePixelRatio,
        }
    }''')

    print(dimensions)
    # >>> {'width': 800, 'height': 600, 'deviceScaleFactor': 1}
    await browser.close()


asyncio.get_event_loop().run_until_complete(scrapeWithPup())


def scrape():
    print("I'm working...")
    resp = uReq("http://www.google.com")
    pageHtml = resp.read()
    resp.close()
    page_soup = soup(pageHtml, "html.parser")

    print(page_soup)


# schedule.every(10).seconds.do(scrape)

# while True:
#     schedule.run_pending()
#     time.sleep(5)
