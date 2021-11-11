#!/bin/bash
#python3 -m venv ".venv"
source .venv/bin/activate
#python -m pip install --upgrade --force-reinstall --disable-pip-version-check pip
#brew services restart postgresql
#python -m pip install --force-reinstall --disable-pip-version-check -r requirement.txt
#django-admin startproject d42 .
#python manage.py makemigrations
#python manage.py migrate
#python3 manage.py startapp ex00
python3 manage.py runserver
