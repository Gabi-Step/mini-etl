import tempfile
import os
import pytest
from flask import current_app
from mini_etl import create_app
from mini_etl.db import get_db


@pytest.fixture()
def app():
    db_fd, db_path = tempfile.mkstemp()

    app = create_app({"TESTING": True, "DATABASE": db_path})

    with app.app_context():
        with get_db() as conn:
            with current_app.open_resource('schema.sql') as f:
                conn.executescript(f.read().decode('utf8'))
            with current_app.open_resource('demo_data/data.sql') as f:
                conn.executescript(f.read().decode('utf8'))

    yield app

    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture()
def client(app):
    return app.test_client()