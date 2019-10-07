#!/bin/bash
set -e

while !</dev/tcp/db/5432
do 
    echo "Waiting for postgres server"
    sleep 1
done

python manage.py collectstatic --no-input

gunicorn eventuality.wsgi -b 0.0.0.0:8000
