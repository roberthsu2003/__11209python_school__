from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    print("debug")
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'