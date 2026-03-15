import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from werkzeug.security import check_password_hash, generate_password_hash

from mini_etl.db import get_db

bp = Blueprint('customers', __name__, url_prefix='/customers')

@bp.route('/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):

    db = get_db()
    customer = db.execute(
        'SELECT * FROM customers WHERE id = ?', (customer_id,)
    ).fetchone()

    if customer is None:
        return {'error': 'Customer not found'}, 404

    return customer