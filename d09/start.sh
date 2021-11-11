#!/bin/bash
python3 -m venv ".venv"
source .venv/bin/activate
python -m pip install --upgrade --force-reinstall --disable-pip-version-check pip
brew services restart postgresql
python -m pip install --force-reinstall --disable-pip-version-check -r requirement.txt
#django-admin startproject d9 .
python manage.py makemigrations 
python manage.py migrate --run-syncdb
#python3 manage.py startapp chat
python3 manage.py createsuperuser
#python3 manage.py shell
docker run -p 6379:6379 -d redis:5
python3 manage.py runserver
