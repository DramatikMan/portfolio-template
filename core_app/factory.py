import os

from flask import Flask, render_template, redirect, url_for

from . import celery, send_email
from .celery_utils import init_celery
from .forms import MessageForm


def create_app():
    app = Flask('core_app')

    cfg = f"config.{os.environ.get('FLASK_ENV').capitalize()}Config"
    app.config.from_object(cfg)
    app.url_map.strict_slashes = False

    init_celery(celery, app)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/contact', methods=['GET', 'POST'])
    def contact():
        form = MessageForm()

        if form.validate_on_submit():
            send_email(form.address.data, form.text.data)
            return redirect(url_for('index'))

        return render_template('contact.html', form=form)

    return app
