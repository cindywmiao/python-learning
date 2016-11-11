from flask import Flask
from flask import request
import flask
app = Flask(__name__)

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            print(request.form['username'])
            print(request.form['password'])
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return flask.render_template('hello.html', error=error)

def valid_login(username, password):
    return username == password

def log_the_user_in(username):
    print(username)

if __name__ == "__main__":
    app.run()