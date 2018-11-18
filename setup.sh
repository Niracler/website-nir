#!/bin/sh

python3 manage.py migrate

python3 manage.py makemigrations

gunicorn -w4 -b 0.0.0.0:8000 website_py.wsgi
