from todo_app.application import create_app
from todo_app.config import create_config
from todo_app.db import create_db

config = create_config(__path__[0])
db = create_db()

from todo_app.views import bp_root

blueprints = [bp_root]

app = create_app(config, db, blueprints)
