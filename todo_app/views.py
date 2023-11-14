from flask import Blueprint, render_template
from flask.typing import ResponseReturnValue

bp_root = Blueprint("root", __name__, url_prefix="/")
bp_tasks = Blueprint("tasks", __name__, url_prefix="/tasks")


@bp_root.route("/")
def index() -> ResponseReturnValue:
    return render_template("index.html")
