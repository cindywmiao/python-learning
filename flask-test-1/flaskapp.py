from flask import Flask, render_template
from model import User

app = Flask(__name__)

@app.route('/')
def hello_world():
    content = "Hello World"
    return render_template("index.html", content=content)

@app.route('/user')
def user_index():
    user = User(1, "cindy")
    return render_template("user.html", user=user)

@app.route('/query_user/<user_id>')
def query_user(user_id):
    user = None
    if int(user_id) == 1:
        user = User(1, 'cindy')
    return render_template("user_id.html", user = user)

@app.route('/users')
def user_list():
    users = []
    for i in range(1, 11):
        user = User(i, 'cindy' + str(i))
        users.append(user)

    return render_template("user_list.html", users = users)

@app.route('/one')
def one_page():
    return render_template("one.html")

@app.route('/two')
def two_page():
    return render_template("two.html")

if __name__ == '__main__':
    app.run()