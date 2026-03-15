import os

from flask import Flask

from mini_etl.cli import add_app_commands


def create_app(test_config=None) -> Flask:
    """Example of flask set up adapted from: https://flask.palletsprojects.com/en/stable/tutorial/factory/"""
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    os.makedirs(app.instance_path, exist_ok=True)

    add_app_commands(app)
    from mini_etl.api import customers
    app.register_blueprint(customers.bp)

    return app