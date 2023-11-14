from flask import Blueprint, redirect, render_template, request, url_for
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


@bp_tasks.route("/create", methods=["GET", "POST"])
def create() -> ResponseReturnValue:
    if request.method == "POST":
        task = Tasks(
            title=request.form["title"],
            description=request.form["description"],
            open=True,
        )
        db.session.add(task)
        db.session.commit()
        return redirect(url_for("tasks.get"))

    return render_template("tasks_create.html")


@bp_tasks.route("/<int:id>/update", methods=["GET", "POST"])
def update_by_id(id: int) -> ResponseReturnValue:
    task = db.get_or_404(Tasks, id)

    if request.method == "POST":
        task.title = request.form["title"]
        task.description = request.form["description"]
        db.session.add(task)
        db.session.commit()
        return redirect(url_for("tasks.get"))

    return render_template("tasks_update_by_id.html", task=task)


@bp_tasks.route("/<int:id>/close", methods=["GET"])
def close_by_id(id: int) -> ResponseReturnValue:
    task = db.get_or_404(Tasks, id)

    task.open = False

    db.session.add(task)
    db.session.commit()
    return render_template("tasks_close_by_id.html", task=task)


@bp_tasks.route("/<int:id>/open", methods=["GET"])
def open_by_id(id: int) -> ResponseReturnValue:
    task = db.get_or_404(Tasks, id)

    task.open = True

    db.session.add(task)
    db.session.commit()
    return render_template("tasks_open_by_id.html", task=task)


@bp_tasks.route("/<int:id>/delete", methods=["GET"])
def delete_by_id(id: int) -> ResponseReturnValue:
    task = db.get_or_404(Tasks, id)
    db.session.delete(task)
    db.session.commit()
    return render_template("tasks_delete_by_id.html", task=task)
