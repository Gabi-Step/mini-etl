import click
from flask import current_app

from mini_etl.db import get_db
from mini_etl.order_totals import customer_total_orders_value


def load_data():
    with get_db() as conn:
        with current_app.open_resource('demo_data/data.sql') as f:
            conn.executescript(f.read().decode('utf8'))


def init_db():
    with get_db() as conn:
        with current_app.open_resource('schema.sql') as f:
            conn.executescript(f.read().decode('utf8'))


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


@click.command('load-demo-data')
def load_demo_data():
    try:
        load_data()
    except Exception as e:
        click.echo(f'Failed to load demo data: {e}')
        return
    click.echo('Loading demo data completed.')


@click.command('demo-script-run')
def demo_script_run():
    try:
        with get_db() as conn:
            customer_total_orders_value(conn)
    except Exception as e:
        click.echo(f'Failed to run customer_total_orders_value: {e}')
        return
    click.echo('Customer_total_orders_value script completed successfully.')


def add_app_commands(app) -> None:
    app.cli.add_command(init_db_command)
    app.cli.add_command(load_demo_data)
    app.cli.add_command(demo_script_run)
