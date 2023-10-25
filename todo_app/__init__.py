from flask import Flask
from flask.config import Config
from flask_sqlalchemy import SQLAlchemy

from todo_app.config import create_config
from todo_app.db import create_db
from todo_app.views import bp_root

config = create_config(__path__[0])
db = create_db()


def create_app(config: Config, db: SQLAlchemy) -> Flask:
    app = Flask(__name__)
    app.config = config

    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.register_blueprint(bp_root)

    return app


app = create_app(config, db)
