from flask import Blueprint,render_template,request
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

blueprint_auth = Blueprint('auth', __name__,url_prefix='/auth')

@blueprint_auth.route('/',methods=['GET', 'POST'])
@blueprint_auth.route('/login',methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        print(request.form['email'])
        print(request.form['password'])
    

    return render_template("/auth/login.html")