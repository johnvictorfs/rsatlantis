#!/usr/bin/env bash

# Front-end Build #
cd frontend/

npm install || exit_on_error "Could not install npm dependencies"
npm run build || exit_on_error "Could not build Vue Bundle"
cd ..

# Back-end Build
cd backend/

poetry install || exit_on_error "Could not install pyproject.toml dependencies"
poetry shell|| exit_on_error "Could not load shell with python venv using Poetry"
python manage.py migrate || exit_on_error "Could not migrate DB changes correctly"
python manage.py test || exit_on_error "Failure when running tests"
python manage.py collectstatic || exit_on_error "Could not run collectstatic management command"