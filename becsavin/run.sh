#!/bin/sh

python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate
gunicorn becsavin.wsgi --bind=0.0.0.0:80
