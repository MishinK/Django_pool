#!/bin/bash
python3 -m venv ".venv"
source .venv/bin/activate
pip install --force-reinstall -r requirement.txt
#django-admin startproject Rush00 .
#python manage.py migrate
#python3 manage.py startapp moviemon
python3 manage.py runserver
