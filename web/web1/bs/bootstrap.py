from flask import Blueprint,render_template

bp = Blueprint('bs', __name__, url_prefix='/bs')

@bp.route("/")
def index():
    return render_template("bs/index.html")

@bp.route("/product")
def product():
    return render_template("bs/product.html")

@bp.route("/profile")
def profile():
    return render_template("bs/profile.html")