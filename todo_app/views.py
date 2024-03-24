import functools

from flask import (
    Blueprint,
    abort,
    flash,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from flask.typing import ResponseReturnValue
from sqlalchemy.exc import NoResultFound
from typing import Any
from werkzeug.security import check_password_hash

from todo_app import db
from todo_app.db import Tasks, Users

bp_root = Blueprint("root", __name__, url_prefix="/")
bp_tasks = Blueprint("tasks", __name__, url_prefix="/tasks")
bp_auth = Blueprint("auth", __name__, url_prefix="/auth")


# load user from session for blueprint root
@bp_root.before_app_request
@bp_tasks.before_app_request
def load_logged_in_user() -> None:
    user_id = session.get("user_id")

    if user_id is None:
        g.user = None
    else:
        g.user = db.session.execute(db.select(Users).filter_by(id=user_id)).scalar_one()


# view decorator to require login
def login_required(view: Any) -> Any:
    @functools.wraps(view)
    def wrapped_view(**kwargs: Any) -> Any:
        if g.user is None:
            return redirect(url_for("auth.login"))

        return view(**kwargs)

    return wrapped_view


@bp_root.route("/")
def index() -> ResponseReturnValue:
    return render_template("index.html")


@bp_tasks.route("/", methods=["GET"])
@login_required
def get() -> ResponseReturnValue:
    tasks = db.session.execute(db.select(Tasks).filter_by(user_id=g.user.id)).scalars()
    return render_template("tasks_get.html", tasks=tasks)


@bp_tasks.route("/<int:id>", methods=["GET"])
@login_required
def get_by_id(id: int) -> ResponseReturnValue:
    try:
        task = db.session.execute(db.select(Tasks).filter_by(id=id).filter_by(user_id=g.user.id)).scalar_one()
    except NoResultFound:
        abort(404)
    return render_template("tasks_get_by_id.html", task=task)


@bp_tasks.route("/create", methods=["GET", "POST"])
@login_required
def create() -> ResponseReturnValue:
    if request.method == "POST":
        task = Tasks(
            title=request.form["title"],
            description=request.form["description"],
            open=True,
            user_id=g.user.id,
        )
        db.session.add(task)
        db.session.commit()
        return redirect(url_for("tasks.get"))

    return render_template("tasks_create.html")


@bp_tasks.route("/<int:id>/update", methods=["GET", "POST"])
@login_required
def update_by_id(id: int) -> ResponseReturnValue:
    try:
        task = db.session.execute(db.select(Tasks).filter_by(id=id).filter_by(user_id=g.user.id)).scalar_one()
    except NoResultFound:
        abort(404)

    if request.method == "POST":
        task.title = request.form["title"]
        task.description = request.form["description"]
        db.session.add(task)
        db.session.commit()
        return redirect(url_for("tasks.get"))

    return render_template("tasks_update_by_id.html", task=task)


@bp_tasks.route("/<int:id>/close", methods=["GET"])
@login_required
def close_by_id(id: int) -> ResponseReturnValue:
    try:
        task = db.session.execute(db.select(Tasks).filter_by(id=id).filter_by(user_id=g.user.id)).scalar_one()
    except NoResultFound:
        abort(404)

    task.open = False

    db.session.add(task)
    db.session.commit()
    return render_template("tasks_close_by_id.html", task=task)


@bp_tasks.route("/<int:id>/open", methods=["GET"])
@login_required
def open_by_id(id: int) -> ResponseReturnValue:
    try:
        task = db.session.execute(db.select(Tasks).filter_by(id=id).filter_by(user_id=g.user.id)).scalar_one()
    except NoResultFound:
        abort(404)

    task.open = True

    db.session.add(task)
    db.session.commit()
    return render_template("tasks_open_by_id.html", task=task)


@bp_tasks.route("/<int:id>/delete", methods=["GET"])
@login_required
def delete_by_id(id: int) -> ResponseReturnValue:
    try:
        task = db.session.execute(db.select(Tasks).filter_by(id=id).filter_by(user_id=g.user.id)).scalar_one()
    except NoResultFound:
        abort(404)
    db.session.delete(task)
    db.session.commit()
    return render_template("tasks_delete_by_id.html", task=task)


@bp_auth.route("/login", methods=("GET", "POST"))
def login() -> ResponseReturnValue:
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        try:
            user = db.session.execute(db.select(Users).filter_by(username=username)).scalar_one()
        except NoResultFound:
            flash("Authentication failed. Please try again.")

        if user.username == username and check_password_hash(user.password, password):
            session.clear()
            session["user_id"] = user.id
            return redirect(url_for("root.index"))
        flash("Authentication failed. Please try again.")

    return render_template("auth_login.html")


@bp_auth.route("/logout", methods=["GET"])
def logout() -> ResponseReturnValue:
    session.clear()
    return redirect(url_for("root.index"))
