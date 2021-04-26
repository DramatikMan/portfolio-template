pipenv run celery -A celery_runner.celery worker --detach
pipenv run aiosmtpd --listen 127.0.0.1:8025 & disown
pipenv run devserver
