from flask import Flask

from .config import create_config
from .db import create_db


def create_app() -> Flask:
    app = Flask(__name__)
    app.config = create_config(app.root_path)

    db = create_db()
    db.init_app(app)

    return app


app = create_app()
