from flask import Blueprint, render_template, abort,redirect,request
from jinja2 import TemplateNotFound
from flask_wtf import FlaskForm
from wtforms import PasswordField,EmailField,StringField,SelectField
from wtforms.validators import DataRequired,Length,Regexp

register_blue = Blueprint('register',__name__,url_prefix='/auth')

class UserRegistrationForm(FlaskForm):
    uName = StringField("姓名",validators=[DataRequired(),Length(min=2, max=10)])
    uGender = SelectField("性別", choices=[("男", "男"), ("女", "女"), ("其它","其它")])
    uPhone = StringField("聯絡電話",validators=[DataRequired(),Regexp(r'\d\d\d\d-\d\d\d-\d\d\d',message="格式不正確")])

@register_blue.route("/register",methods=['GET','POST'])
def register():
    form = UserRegistrationForm()
    if request.method == "POST":
        print("post")
        if form.validate_on_submit():
            uName = request.form['uName']
            print("姓名=",uName)

            uGender = form.uGender.data
            print("性別=",uGender)            

            uPhone = form.uPhone.data
            print("電話=",uPhone)
            
        else:
            print("驗證失敗")
    else:
        print("第一次進入")
    return render_template("auth/register.html",form=form)



class MyForm(FlaskForm):
    email = EmailField('郵件信箱',validators=[DataRequired()])
    password = PasswordField('密碼',validators=[DataRequired()])    

@register_blue.route("/login",methods=['GET','POST'])
def login():
    form = MyForm()
    if request.method == "POST":
        if form.validate_on_submit():
            print("驗證成功")
            return redirect('/auth/success')
        else:
            print("驗證失敗")      
        
    else:
        print("第一次進入")

    return render_template("auth/login.html",form = form)

@register_blue.route('/success')
def success():
    return render_template('auth/success.html')