evs=(
	FLASK_APP
	FLASK_ENV
	SMTP_SENDER
	SMTP_PASSWORD
	SECRET_KEY
	CELERY_BROKER_URL
	CELERY_RESULT_BACKEND
)
for variable in "${evs[@]}"; do
	if [[ -z ${!variable+x} ]] || [[ -z ${!variable} ]] ; then
		echo -e "\e[93mEnvironmental variable \e[1m$variable\e[21m is not defined or is empty.\e[0m"
		((undef++))
	fi
done
if [[ $undef -gt 0 ]]; then exit 1; fi

pipenv install gunicorn

echo $'
workers=4
bind="unix:/tmp/core_app/gunicorn.sock"
wsgi_app="core_app.factory:create_app()"' > gunicorn.conf.py

source .venv/bin/activate
gunicorn
