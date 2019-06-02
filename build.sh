#!/usr/bin/env bash

# Front-end Build #
cd frontend/

yarn install || exit 1 "Could not install npm dependencies"
build || exit 1 "Could not build Vue Bundle"
cd ..

# Back-end Build
cd backend/

poetry install || exit 1 "Could not install pyproject.toml dependencies"
poetry run python manage.py migrate || exit 1 "Could not migrate DB changes correctly"
poetry run python manage.py test || exit 1 "Failure when running tests"
poetry run python manage.py collectstatic --noinput || exit 1 "Could not run collectstatic management command"