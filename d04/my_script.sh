#!/bin/sh
/usr/bin/python3 -m venv django_venv
source django_venv/bin/activate
python -m pip install --force-reinstall --disable-pip-version-check -r requirements.txt
#django-admin startproject d04 .
#python manage.py makemigrations --merge
#python manage.py startapp ex00
#python manage.py startapp ex01
#python manage.py startapp ex02
#python manage.py startapp ex03
#python manage.py collectstatic
python manage.py runserver