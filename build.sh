#!/usr/bin/env bash

ORANGE=$'\e[33m'
GREEN=$'\e[32m'
RED=$'\e[31m'
NC=$'\e[0m'

# Front-end Build #
cd frontend/

yarn install || echo "${RED}Could not install npm dependencies${NC}" && exit 1
yarn build || echo "${RED}Could not build Vue Bundle${NC}" && exit 1
cd ..

# Back-end Build
cd backend/

poetry install || echo "${RED}Could not install pyproject.toml dependencies${NC}" && exit 1
poetry run python manage.py migrate || echo "${RED}Could not migrate DB changes correctly${NC}" && exit 1
poetry run python manage.py test || echo "${RED}Failure when running tests${NC}" && exit 1
poetry run python manage.py collectstatic --noinput || echo "${RED}Could not run collectstatic management command${NC}" && exit 1