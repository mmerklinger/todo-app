from flask import Blueprint, render_template
from flask.typing import ResponseReturnValue

from todo_app import db
from todo_app.db import Tasks

bp_root = Blueprint("root", __name__, url_prefix="/")
bp_tasks = Blueprint("tasks", __name__, url_prefix="/tasks")


@bp_root.route("/")
def index() -> ResponseReturnValue:
    return render_template("index.html")


@bp_tasks.route("/", methods=["GET"])
def get() -> ResponseReturnValue:
    tasks = db.session.execute(db.select(Tasks)).scalars()
    return render_template("tasks_get.html", tasks=tasks)


@bp_tasks.route("/<int:id>", methods=["GET"])
def get_by_id(id: int) -> ResponseReturnValue:
    task = db.get_or_404(Tasks, id)
    return render_template("tasks_get_by_id.html", task=task)
