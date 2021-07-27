import pytest

from main import app as flask_app  ##


@pytest.fixture
def app():
      app = flask_app
      return app
