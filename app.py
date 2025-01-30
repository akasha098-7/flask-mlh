import sys
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World! Welcome to magic shop!"

@app.route('/about')
def about():
    return "This is the About this shop, here you can have a cup of warm tea and look above the galaxy! Here you can heal you!"

@app.route('/greet/<username>')
def greet_user(username):
    return f"Hello, {username}! Welcome to magic shop!."

@app.route('/user/<int:user_id>')
def show_user_profile(user_id):
    return f"User Profile Page for User ID: {user_id}"

@app.route('/all')
def all_pages():
    home_content = home()
    about_content = about()
    greet_content = greet_user("Guest")
    user_profile_content = show_user_profile(1)
    return f"""
    <h1>Home</h1>
    <p>{home_content}</p>
    <h1>About</h1>
    <p>{about_content}</p>
    <h1>Greet</h1>
    <p>{greet_content}</p>
    <h1>User Profile</h1>
    <p>{user_profile_content}</p>
    """

if __name__ == '__main__':
    app.run(debug=True)
