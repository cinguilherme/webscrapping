import bs4

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

resp = uReq("http://www.google.com")
pageHtml = resp.read()
resp.close()

page_soup = soup(pageHtml, "html.parser")

print(page_soup)
print("playgorund ran successfully")
