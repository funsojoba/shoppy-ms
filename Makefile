COMPOSE = docker-compose -f docker-compose.yaml

up:
	$(COMPOSE) up

down:
	$(COMPOSE) down

build:
	$(COMPOSE) build

start:
	$(COMPOSE) start