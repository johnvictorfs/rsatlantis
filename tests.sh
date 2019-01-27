#!/usr/bin/env bash

# Script to run all tests of the project

cd backend/
poetry install
poetry run python manage.py test
