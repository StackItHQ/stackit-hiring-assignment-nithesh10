from flask import jsonify, render_template, request, redirect, url_for, flash
import pandas as pd
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
        return redirect(url_for('display_csv', filename_without_extension=filename_without_extension))


@app.route('/display_csv/<filename_without_extension>', methods=['GET', 'POST'])
def display_csv(filename_without_extension):
    filepath=os.path.join(app.config['UPLOAD_FOLDER'], (filename_without_extension+".csv"))
    if request.method == 'POST':
        selected_columns = request.form.getlist('selected_columns')
        # Pass the selected columns to the import_csv function
        result = gsheets.import_csv(filename_without_extension, filepath, selected_columns)
        return redirect((result))
    df = pd.read_csv(filepath)
    columns = df.columns.tolist()
    # Render the template to display the DataFrame
    return render_template('display_csv.html', df=df, columns=columns,filename=filename_without_extension)

@app.route('/apply_filters/', methods=['POST'])
def apply_filters():
    try:
        filter_data = request.get_json()
        applied_filters = filter_data.get("appliedFilters")
        file_name = filter_data.get("filename")
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], (file_name + ".csv"))
        df = pd.read_csv(filepath)

        for applied_filter in applied_filters:
            parts = applied_filter.split()
            column = parts[0]
            filter_type = parts[1]
            value = ' '.join(parts[2:])
            print(column,filter_type,value)
            if filter_type == "exact":
                df = df[df[column] == value]
                
            elif filter_type == "not_exact":
                df = df[df[column] != value]
                
            elif filter_type == "start_with":
                df = df[df[column].str.startswith(value)]

            elif filter_type == "greater_than":

                df = df[df[column] > int(value)]
            
            elif filter_type == "less_than":
                df = df[df[column] < int(value)]
                
            elif filter_type == "greater_than_equals":
                df = df[df[column] >= int(value)]
                
            elif filter_type == "less_than_equals":
                df = df[df[column] <= int(value)]
        
        df=df.reset_index(drop=True)
        print(df)
        return jsonify({"filtered_data": df.to_json()})
    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == '__main__':
    app.run()
