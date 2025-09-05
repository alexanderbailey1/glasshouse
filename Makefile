.RECIPEPREFIX := >
.PHONY: init up down logs dbshell

init:
>docker compose build

up:
>docker compose up -d

down:
>docker compose down

logs:
>docker compose logs -f

dbshell:
>docker compose exec db psql -U postgres glasshouse
