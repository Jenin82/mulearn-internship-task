#!/bin/bash
python manage.py migrate --noinput
gunicorn --bind 0.0.0.0:8000 mulearn-internship-task.wsgi
