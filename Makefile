.PHONY: build up down shell test

build:
	docker-compose build

up:
	docker-compose up

upd:
	docker-compose up -d

down:
	docker-compose down

shell:
	docker-compose exec -it web bash

test:
	docker-compose exec web python manage.py test

run-debug:
	docker-compose run --rm --service-ports web
