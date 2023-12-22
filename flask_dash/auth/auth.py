from flask import Blueprint,render_template,request,redirect
from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,EmailField,BooleanField,DateField,TextAreaField,PasswordField
from wtforms.validators import DataRequired,Length,Regexp,Optional,EqualTo

blueprint_auth = Blueprint('auth', __name__,url_prefix='/auth')

class MyForm(FlaskForm):
    name = StringField('姓名', validators=[DataRequired()])

@blueprint_auth.route('/',methods=['GET', 'POST'])
@blueprint_auth.route('/login',methods=['GET', 'POST'])
def login():
    form = MyForm()
    if request.method == "POST" and form.validate_on_submit():     
        if request.form['name'] == "12345" and request.form['password'] == "12345":
            print("密碼正確")
            return redirect("/auth/success")
        else:
            print("密碼錯誤")
    

    return render_template("/auth/login.html",form=form)

@blueprint_auth.route('/success')
def success():
    return render_template('/auth/success.html')

class UserRegistrationForm(FlaskForm):
    uName = StringField("姓名",validators=[DataRequired(message="此欄必需有資料"),Length(min=2,max=20)])
    uGender = SelectField("性別",choices=[("女","女"),("男","男"),("其它","其它")])
    uPhone = StringField("聯絡電話",validators=[Regexp(r'\d\d\d\d-\d\d\d-\d\d\d',message="格式不正確")])
    uEmail = EmailField("電子郵件",validators=[DataRequired()])
    isGetEmail = BooleanField("接受促銷email",default=False)
    uBirthday = DateField("出生年月日",validators=[Optional()],format='%Y-%m-%d')
    uAboutMe = TextAreaField('自我介紹', [Optional(), Length(max=200)])
    uPass = PasswordField("密碼",validators=[DataRequired(),Length(min=4,max=20),EqualTo('uConfirmPass',message='驗証密碼不正確')])
    uConfirmPass = PasswordField("驗証密碼",validators=[DataRequired(),Length(min=4,max=20)])
    


@blueprint_auth.route('/registor',methods=['GET','POST'])
def register():
    form = UserRegistrationForm()
    if request.method == "POST":
        if form.validate_on_submit():
            uName = form.uName.data
            form.uName.data = ''
            print("姓名",uName)

            uGender = form.uGender.data
            print("性別",uGender)

            uPhone = form.uPhone.data
            print("手機號碼",uPhone)

            uEmail = form.uEmail.data
            print("email:",uEmail)

            isGetEmail = form.isGetEmail.data
            print("接受促銷","接受" if isGetEmail else "不接受")

            uBirthday = form.uBirthday.data
            print("出生",uBirthday)

            uAboutMe = form.uAboutMe.data
            print("自我介紹",uAboutMe)

            uPass = form.uPass.data
            print("密碼",uPass)
            
        else:
            print("驗證失敗")

    return render_template('/auth/registor.html',form=form)