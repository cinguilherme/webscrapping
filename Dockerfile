from python:3.8

RUN pip install bs4 schedule pyppeteer

COPY . /app
