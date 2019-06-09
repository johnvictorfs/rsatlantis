#!/usr/bin/env bash

ORANGE=$'\e[33m'
GREEN=$'\e[32m'
RED=$'\e[31m'
NC=$'\e[0m'

# Front-end Build #
cd frontend/

if ! yarn install ; then
  echo "${RED}Could not install npm dependencies${NC}"
  exit 1
fi

if ! yarn lint --fix ; then
  echo "${RED}Failed front-end linting tests${NC}"
  exit 1
fi

if ! yarn build ; then
  echo "${RED}Could not build Vue Bundle${NC}"
  exit 1
fi

# Back-end Build
cd ../backend/

if ! poetry install ; then
  echo "${RED}Could not install pyproject.toml dependencies${NC}"
  exit 1
fi
if ! poetry run python manage.py migrate ; then
  echo "${RED}Could not migrate DB changes correctly${NC}"
  exit 1
fi
if ! poetry run python manage.py test ; then
  echo "${RED}Failure when running tests${NC}"
  exit 1
fi
if ! poetry run python manage.py collectstatic --noinput ; then
  echo "${RED}Could not run collectstatic management command${NC}"
  exit 1
fi
