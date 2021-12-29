export DJANGO_SETTINGS_MODULE=config.settings.deploy

python manage.py makemigrations replay && \
python manage.py migrate && \
echo yes | python manage.py collectstatic && \

gunicorn --log-level=DEBUG --bind 0.0.0.0:8000 --timeout 1200 config.wsgi.deploy:application
