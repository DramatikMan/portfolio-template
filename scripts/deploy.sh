evs=(
	FLASK_APP
	FLASK_ENV
	SMTP_SENDER
	SMTP_PASSWORD
	SECRET_KEY
	CELERY_BROKER_URL
	# CELERY_RESULT_BACKEND
)
for variable in "${evs[@]}"; do
	if [[ -z ${!variable+x} ]] || [[ -z ${!variable} ]] ; then
		echo -e "\e[93mEnvironmental variable \e[1m$variable\e[21m is undefined or empty.\e[0m"
		((undef++))
	fi
done
if [[ $undef -gt 0 ]]; then exit 1; fi

pipenv install gunicorn

echo $'
workers=4
bind="0.0.0.0:8000"
wsgi_app="core_app.factory:create_app()"' > gunicorn.conf.py

source .venv/bin/activate
pipenv run celery -A celery_runner.celery worker --detach
gunicorn
