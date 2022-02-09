#! /bin/sh

python /usr/src/inno_test/manage.py migrate --noinput 
python /usr/src/inno_test/manage.py runserver 0.0.0.0:8000