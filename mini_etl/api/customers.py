"""Customers API.
Adapted from: https://flask.palletsprojects.com/en/stable/tutorial/views/,
https://stackoverflow.com/questions/40883669/flask-restful-api-using-get-to-get-a-specific-id-and-returning-201-using-python
"""
from flask import Blueprint, jsonify

from mini_etl.db import get_db

bp = Blueprint('customers', __name__, url_prefix='/customers')


@bp.route('/<int:customer_id>', methods=['GET'])
def get_customer(customer_id: int):
    """Get a customer and their orders by ID."""

    with get_db() as conn:
        customer = conn.execute(
            'SELECT * FROM customers WHERE id = ?', (customer_id,)
        ).fetchone()

    if customer is None:
        return {'error': 'Customer not found'}, 404

    with get_db() as conn:
        orders = conn.execute(
            'SELECT * FROM orders WHERE customer_id = ?', (customer_id,)
        ).fetchall()

    return jsonify({
        **dict(customer),
        'orders': [dict(order) for order in orders]
    })