from flask import Flask, render_template, request, url_for, redirect, flash
from werkzeug.routing import BaseConverter
from werkzeug.utils import secure_filename
from os import path

class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]

app = Flask(__name__)
app.url_map.converters['regex'] = RegexConverter

@app.route('/')
def hello_world():
    return render_template('index.html', title='Welcome')


@app.route('/services')
def services():
    return 'Services'


@app.route('/about')
def about():
    return 'About'


@app.route('/user_name/<regex("[a-z]:{3}"):user_name>')
def user_name(user_name):
    return 'User %s' % user_name


@app.route('/user_id/<int:user_id>')
def user_id(user_id):
    return 'User : %s' % user_id


@app.route('/projects/')
@app.route('/our-works/')
def projects():
    return 'The project page'


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username=request.form['username']
        password=request.form['password']
    else:
        username=request.args['username']
        password=request.args['password']
    return render_template('login.html', method=request.method)


# @app.route('/upload', methods=['GET','POST'])
# def upload():
#     if request.method=='POST':
#         print('Here')
#         f = request.files['file']
#         basepath = path.abspath(path.dirname(__file__))
#         upload_path=path.join(basepath, 'static/uploads/')
#         f.save(upload_path, secure_filename(f.filename))
#         return redirect(url_for('upload'))
#     else:
#         print("There")
#     return render_template('upload.html')

UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        print('Here')
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)