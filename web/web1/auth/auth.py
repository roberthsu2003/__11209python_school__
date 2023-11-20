from flask import Blueprint
bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route("/")
def index():
    return "<h1>Hello! World!</h1>"

@bp.route("/login")
def login():
    return "<h1>Login</h1>"