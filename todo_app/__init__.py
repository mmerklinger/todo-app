from flask import Flask

from todo_app.config import create_config
from todo_app.db import create_db
from todo_app.views import bp_root


def create_app() -> Flask:
    app = Flask(__name__)
    app.config = create_config(app.root_path)

    db = create_db()
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.register_blueprint(bp_root)

    return app


app = create_app()
