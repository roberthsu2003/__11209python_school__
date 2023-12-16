from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

register_blue = Blueprint('register',__name__,url_prefix='/auth')
@register_blue.route("/register")
def register():
    return render_template("auth/register.html")

@register_blue.route("/login")
def login():
    return render_template("auth/login.html")