from flask import Flask

from .config import create_config


def create_app() -> Flask:
    app = Flask(__name__)
    app.config = create_config(app.root_path)
    return app


app = create_app()
