from flask import Blueprint,render_template

bp = Blueprint('bs', __name__, url_prefix='/bs')

@bp.route("/")
def index():
    return render_template("bs/index.html")