from flask import Blueprint, render_template, abort,redirect
from jinja2 import TemplateNotFound
from flask_wtf import FlaskForm
from wtforms import PasswordField,EmailField
from wtforms.validators import DataRequired

register_blue = Blueprint('register',__name__,url_prefix='/auth')
@register_blue.route("/register")
def register():
    return render_template("auth/register.html")



class MyForm(FlaskForm):
    email = EmailField('郵件信箱',validators=[DataRequired()])
    password = PasswordField('密碼',validators=[DataRequired()])
    
    

@register_blue.route("/login",methods=['GET','POST'])
def login():
    form = MyForm()
    if form.validate_on_submit():
        print("成功")
        return redirect('/auth/success')
    else:
        print("第一次執行 or 失敗")

    return render_template("auth/login.html",form = form)

@register_blue.route('/success')
def success():
    return render_template('auth/success.html')