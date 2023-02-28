#!/bin/sh
export DJANGO_SETTINGS=prod
touch /app/log/kartonpmv.log
cd /app

if [ "$#" -ne 0 ]; then
  echo "python3 manage.py" "$@"
  python3 manage.py "$@"
else
  python3 manage.py migrate
  gunicorn -b 0.0.0.0:8000 -w 2 --access-logfile log/gunicorn.log kartonpmv.wsgi:application
fi
