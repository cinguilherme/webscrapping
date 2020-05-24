### attenction: read the robots.txt of any site before scrapping it!

## requirements

#### there is 3 ways to work here, Scrapy, BeatyfulSoup and Puppetter

```
docker, docker compose and Make
```

### To build the image

```
make build
```

#### requirements.txt is only required for bettern behaving of your IDE since the dependencies will not be available out of your docker image.

### this project is a simplified way to webscraping with spoecific targets

#### for instagram scrapping probably will require somethig abouve the scope of this project

#### for facebook scrapping probably will require somethig abouve the scope of this project. Just read somewere on the web that this is possibly not legal.

##### scrapy sample in the reddit folder

###### the second line will generate a JSON file with all urls for images scraped

```
scrapy runspider XPTO.py -o output.json
scrapy runspider src/reddit/reddidspiders.py -o output.json
```
