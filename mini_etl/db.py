import sqlite3
from datetime import datetime
import pandas as pd

import click
from flask import current_app, g


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES,
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


sqlite3.register_converter(
    "timestamp", lambda v: datetime.fromisoformat(v.decode())
)


def load_data():
    db = get_db()
    with current_app.open_resource('demo_data/data.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('load-demo-data')
def load_demo_data():
    try:
        load_data()
    except Exception as e:
        click.echo(f'Failed to load demo data: {e}')
        return
    click.echo('Loading demo data completed.')


def customer_total_orders_value():
    conn = get_db()
    df = pd.read_sql_query('''
        SELECT o.customer_id, c.first_name, c.last_name, o.quantity, o.price
        FROM orders o
        JOIN customers c ON o.customer_id = c.id
        WHERE c.status = "active"
    ''', conn)

    df['order_value'] = df['quantity'] * df['price']

    totals = df.groupby(['customer_id', 'first_name', 'last_name'])['order_value'].sum().reset_index()
    totals['full_name'] = totals['first_name'] + ' ' + totals['last_name']

    final = totals[['full_name', 'order_value']].rename(columns={'order_value': 'total'})

    final.to_csv(f'.customer_total_orders_value-{datetime.now()}.csv', index=False)


@click.command('demo-script-run')
def demo_script_run():
    try:
        customer_total_orders_value()
    except Exception as e:
        click.echo(f'Failed to run customer_total_orders_value: {e}')
        return
    click.echo('Customer_total_orders_value script completed successfully.')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    app.cli.add_command(load_demo_data)
    app.cli.add_command(demo_script_run)
