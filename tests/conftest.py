import pytest

from core_app.factory import create_app


@pytest.fixture(scope='session')
def app():
    app = create_app()
    return app


@pytest.fixture(scope='session')
def client(app):
    return app.test_client()
