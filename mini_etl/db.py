import sqlite3
from contextlib import contextmanager

from flask import current_app, g


@contextmanager
def get_db():
    conn = sqlite3.connect(current_app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()
