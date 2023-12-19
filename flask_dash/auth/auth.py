from flask import Blueprint

blueprint_auth = Blueprint('auth', __name__,url_prefix='/auth')

@blueprint_auth.route('/')
@blueprint_auth.route('/login')
def login():
    return "<h1>Hello! Login</h1>"