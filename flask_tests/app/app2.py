import os
from flask import Flask, request, redirect, url_for, render_template, flash
from werkzeug.utils import secure_filename
from flask import send_from_directory

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
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
            basepath = os.path.abspath(os.path.dirname(__file__))
            upload_path=os.path.join(basepath, 'static/uploads/')
            file.save(os.path.join(upload_path, filename))
            #flash('Hello', 'info')
            return redirect(url_for('uploaded_file',
                                    filename=filename))

    return render_template('upload.html')


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    basepath = os.path.abspath(os.path.dirname(__file__))
    upload_path = os.path.join(basepath, 'static/uploads/')
    return send_from_directory(upload_path, filename)


if __name__ == '__main__':
    app.run(debug=True)


