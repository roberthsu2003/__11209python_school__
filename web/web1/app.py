from flask import Flask,url_for

app = Flask(__name__)

@app.route('/')
def index():
    print("debug")
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'<h1>User {username}</h1>'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'<h1>Post {post_id * 5}</h1>'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'<h1>Subpath {subpath}</h1>'

@app.route('/url')
def url():
    print(url_for('hello'))
    print(url_for('show_user_profile',username="RobertHsu"))
    print(url_for('static', filename='css/style.css'))
    return "ABC"