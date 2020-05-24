import bs4
import time
import schedule

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

print("playgorund ran successfully")
print("this will keep scraping on a time based")


def scrape():
    print("I'm working...")
    resp = uReq("http://www.google.com")
    pageHtml = resp.read()
    resp.close()
    page_soup = soup(pageHtml, "html.parser")

    print(page_soup)


schedule.every(10).seconds.do(scrape)

while True:
    schedule.run_pending()
    time.sleep(9)
