import os

from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    cfg = f"config.{os.environ.get('FLASK_ENV').capitalize()}Config"
    app.config.from_object(cfg)
    app.url_map.strict_slashes = False

    @app.route('/')
    def index():
        return render_template('index.html')

    return app
