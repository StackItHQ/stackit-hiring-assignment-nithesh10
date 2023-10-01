from flask import render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os

from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash('File uploaded successfully')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
