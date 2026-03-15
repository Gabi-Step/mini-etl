import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from mini_etl.db import get_db

bp = Blueprint('customer', __name__, url_prefix='/customer')