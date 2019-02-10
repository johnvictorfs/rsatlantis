#!/usr/bin/env bash

cd backend/

poetry install || exit_on_error "Could not install pyproject.toml dependencies"
poetry shell|| exit_on_error "Could not load shell with python venv using Poetry"
python manage.py migrate || exit_on_error "Could not migrate DB changes correctly"
python manage.py collectstatic || exit_on_error "Could not run collectstatic management command"
sudo systemctl restart nginx || exit_on_error "Could not restart nginx"