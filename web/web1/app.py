from flask import Flask,url_for,render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    name = "徐國堂"
    age = random_age()
    return render_template('index.html',name=name,age=age)

def random_age():
    return random.randint(25,35)