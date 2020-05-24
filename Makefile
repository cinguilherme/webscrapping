build:
	docker build . -t webscraping_gcc:latest

playground:
	make build && docker-compose run playground
	