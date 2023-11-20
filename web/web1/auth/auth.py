from flask import Blueprint,render_template
bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route("/")
def index():
    return render_template("auth/index.html")

@bp.route("/login")
def login():
    return render_template("auth/login.html")