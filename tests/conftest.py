import pytest

from main import app as flask_app  ##


@pytest.fixture
def app():
      app = flask_app
      return app
    
@pytest.fixture
def client():
    app = flask_app
    client = app.test_client()
    return client