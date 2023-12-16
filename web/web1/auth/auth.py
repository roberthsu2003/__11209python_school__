from flask import Blueprint,render_template,redirect
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired

bp = Blueprint('auth', __name__, url_prefix='/auth')
class LoginForm(FlaskForm):
    name = StringField("姓名",validators=[DataRequired()])
    password = PasswordField("密碼",validators=[DataRequired()])
    submit = SubmitField("確定")

class RegisterForm(FlaskForm):
    name = StringField("姓名",validators=[DataRequired()])
    email = StringField("email",validators=[DataRequired()])
    password = PasswordField("密碼",validators=[DataRequired()])
    confirm = PasswordField("密碼驗證",validators=[DataRequired()])
    submit = SubmitField("確定")

@bp.route("/")
def index():
    return render_template("auth/index.html")

@bp.route("/login",methods=["get","post"])
def login():
    loginForm = LoginForm()
    if loginForm.validate_on_submit():
        return redirect('auth/success')
    return render_template("auth/login.html")

@bp.route("/register",methods=["get","post"])
def register():
    registerForm = RegisterForm()
    if registerForm.validate_on_submit():
        return redirect('auth/success')
    return render_template('auth/register.html',form=registerForm)


@bp.route("/success")
def success():
    return "<h1>登入成功</h1>"