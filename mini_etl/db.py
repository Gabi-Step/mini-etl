"""Database connection helper.
Reference: https://flask.palletsprojects.com/en/stable/tutorial/database/
"""
import sqlite3
from contextlib import contextmanager

from flask import current_app


@contextmanager
def get_db():
    conn = sqlite3.connect(current_app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()
