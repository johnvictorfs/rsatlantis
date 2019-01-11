#!/usr/bin/env bash

# Script to run all tests of the project

cd backend/
pipenv run python manage.py test
