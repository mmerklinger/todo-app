from flask import Blueprint
from flask.typing import ResponseReturnValue

bp_root = Blueprint("root", __name__, url_prefix="/")


@bp_root.route("/")
def index() -> ResponseReturnValue:
    return "Todo-App"
