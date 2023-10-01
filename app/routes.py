from flask import render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os

from app import app
from app.gsheets import gsheets_api  

# Create an instance of the gsheets_api class
gsheets = gsheets_api()

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
        filepath=os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        flash('File uploaded successfully')
        
        filename_without_extension=str(os.path.splitext(filename)[0])
        print("Filename is ",filename_without_extension)
        gsheets.create_new_google_sheet(filename_without_extension)
        selected_columns = ["Column1", "Column2"]
        result = gsheets.import_csv(filename_without_extension, filepath, selected_columns)
        print(result)
        

        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
