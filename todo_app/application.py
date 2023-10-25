from typing import List

from flask import Blueprint, Flask
from flask.config import Config
from flask_sqlalchemy import SQLAlchemy


def create_app(config: Config, db: SQLAlchemy, blueprints: List[Blueprint]) -> Flask:
    app = Flask(__name__)
    app.config = config

    db.init_app(app)
    with app.app_context():
        db.create_all()
    for bp in blueprints:
        app.register_blueprint(bp)

    return app
