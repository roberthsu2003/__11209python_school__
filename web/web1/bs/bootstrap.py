from flask import Blueprint

bp = Blueprint('bs', __name__, url_prefix='/bs')

@bp.route("/")
def index():
    return "<h1>Hello! Bootstraps!</h1>"