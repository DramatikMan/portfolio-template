import os

from flask import Flask, render_template

from . import celery
from .celery_utils import init_celery


def create_app():
    app = Flask('core_app')

    cfg = f"config.{os.environ.get('FLASK_ENV').capitalize()}Config"
    app.config.from_object(cfg)
    app.url_map.strict_slashes = False

    init_celery(celery, app)

    @app.route('/')
    def index():
        return render_template('index.html')

    return app
