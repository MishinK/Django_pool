#!/bin/sh
/usr/bin/python3 -m venv django_venv
source django_venv/bin/activate
python -m pip install --force-reinstall --disable-pip-version-check -r requirement.txt
python Django/manage.py runserver