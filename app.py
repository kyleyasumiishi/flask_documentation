# https://flask.palletsprojects.com/en/1.1.x/quickstart/

from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)
    # What does the %s do?

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)


# I don't understand how the code below works. 
# Specifically, how does it start the app without changing environement variables?
# https://stackoverflow.com/questions/419163/what-does-if-name-main-do

if __name__ == "__main__":
    app.run(debug=True)
