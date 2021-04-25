import os

from core_app import celery
from core_app.factory import create_app
from core_app.celery_utils import init_celery


cfg = f"config.{os.environ.get('FLASK_ENV').capitalize()}Config"
app = create_app()
app.config.from_object(cfg)
init_celery(celery, app)
