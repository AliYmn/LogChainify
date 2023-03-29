.PHONY: build up down shell test

build:
    docker-compose build

up:
    docker-compose up -d

down:
    docker-compose down

shell:
    docker-compose exec web bash

test:
    docker-compose exec web python manage.py test
