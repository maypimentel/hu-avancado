import pytest

from app_factory import create_app


@pytest.fixture(scope='session')
def app():
    app_obj = create_app()
    app_obj.testing = True
    return app_obj


@pytest.fixture
def client(app):
    return app.test_client()


def test_status_code(client):
    resp = client.get('/')
    assert resp.status_code == 200


def test_content(client):
    resp = client.get('/')
    assert 'Hello world' in resp.get_data(as_text=True)
