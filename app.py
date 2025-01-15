import sys
from flask import Flask


sys.stdout = open(sys.stdout.fileno(), mode='w', buffering=1, encoding='utf-8')


app = Flask(__name__)


@app.route('/')
def home():
    return "Hello, World! Welcome to magic shop!"


@app.route('/about')
def about():
    return "This is the About this shop,here you can have a cup of warm tea and look above the galaxy!Here you can heal you!"


@app.route('/greet/<username>')
def greet_user(username):
    return f"Hello, {username}! welcome to magic shop!."


@app.route('/user/<int:user_id>')
def show_user_profile(user_id):
    return f"User Profile Page for User ID: {user_id}"


if __name__ == '__main__':
    app.run(debug=True)
