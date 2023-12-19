from flask import Blueprint,render_template

blueprint_auth = Blueprint('auth', __name__,url_prefix='/auth')

@blueprint_auth.route('/')
@blueprint_auth.route('/login')
def login():
    return render_template("/auth/login.html")