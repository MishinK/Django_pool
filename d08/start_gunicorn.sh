#source .venv/bin/activate
#python manage.py collectstatic --noinput
gunicorn -c gunicorn.conf.py d8.wsgi