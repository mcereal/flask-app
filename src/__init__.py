"""
App creation
"""

import os

from flask import Flask
from . import db


def create_app(test_config=None):
    """App creation function"""
    app = Flask(__name__, instance_relative_config=True)
    db.init_db()

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flask-app.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db.db_session.remove()
    # a simple page that says hello

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
