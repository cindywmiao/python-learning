from flask import Flask, url_for
from flask import request

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()


def do_the_login():
    print "do_the_login"


def show_the_login_form():
    print "show_the_login_form"

if __name__ == "__main__":
    app.run()