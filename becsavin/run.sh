#!/bin/sh

python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate
python manage.py generate_admin_auto
gunicorn becsavin.wsgi --bind=0.0.0.0:80
