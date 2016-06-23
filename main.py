from flask import Flask, render_template, request
from werkzeug import secure_filename

app = Flask(__name__)


@app.route('/upload_new')
def upload():
    return render_template('upload.html')


@app.route('/uploader_new', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return "<h1>file uploaded successfully </h1> \
               <a href='/upload_new'> Back to homepage </a>"


if __name__ == '__main__':
    app.run(debug=True)