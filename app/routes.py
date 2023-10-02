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

@app.route('/workbook-sheet-route', methods=['POST'])
def workbook_sheet_route():
    #try:
        data = request.json
        workbookName = data.get('workbookName')
        workbookOption = data.get('workbookOption')
        sheetName = data.get('sheetName')
        sheetOption = data.get('sheetOption')
        filename=data.get('filename')
        selected_columns=data.get('selectedColumns')
        
       
        if workbookOption == 'create-new':
            gsheets.create_new_google_sheet(workbookName)
        elif workbookOption == 'open-existing':
            gsheets.open_spreadsheet(workbookName)
        
        if sheetOption == 'create-new':
            gsheets.create_new_worksheet(sheetName)
        elif sheetOption == 'use-existing':
            gsheets.open_worksheet(sheetName)
        filepath=os.path.join(app.config['FILTER_FOLDER'], (filename+".csv"))
        result = gsheets.import_csv(filename, filepath, selected_columns)
        print(result)
        response = redirect((result))
        return response

@app.route('/grant_email_access', methods=['POST'])
def grant_email_access():
    data = request.get_json()
    email = data.get('email')
    access_level = data.get('accessLevel')
    gsheets.give_email_access(email,access_level)
    return jsonify({'message': f'Access granted to {email} with {access_level} level'}), 200


@app.route('/generate_sharable_link', methods=['POST'])
def generate_sharable_link():
    access_options = request.json.get('access_options')
    
    spreadsheet_link=gsheets.generate_shareable_link_by_role(access_options)
    response = redirect((spreadsheet_link))
    return response

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
        
        return redirect(url_for('display_csv', filename_without_extension=filename_without_extension))


@app.route('/display_csv/<filename_without_extension>', methods=['GET', 'POST'])
def display_csv(filename_without_extension):
    filepath=os.path.join(app.config['UPLOAD_FOLDER'], (filename_without_extension+".csv"))
    if request.method == 'POST':
        selected_columns = request.form.getlist('selected_columns')
        # Pass the selected columns to the import_csv function
        filepath=os.path.join(app.config['FILTER_FOLDER'], (filename_without_extension+".csv"))
        gsheets.initiate(filename_without_extension)
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
        selected_columns=filter_data.get("selectedcolumns")
        print(selected_columns)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], (file_name + ".csv"))
        df = pd.read_csv(filepath)
        df = df[selected_columns]

        for applied_filter in applied_filters:
            parts = applied_filter.split()
            column = parts[0]
            filter_type = parts[1]
            value = str(' '.join(parts[2:]))
            print(column,filter_type,value)
            if filter_type == "exact":
                df = df[df[column].astype(str) == value]
                
            elif filter_type == "not_exact":
                df = df[df[column].astype(str) != value]
                
            elif filter_type == "start_with":
                df = df[df[column].astype(str).str.startswith(str(value))]

            elif filter_type == "greater_than":

                df = df[df[column] > float(value)]
            
            elif filter_type == "less_than":
                df = df[df[column] < float(value)]
                
            elif filter_type == "greater_than_equals":
                df = df[df[column] >= float(value)]
                
            elif filter_type == "less_than_equals":
                df = df[df[column] <= float(value)]
        
        df=df.reset_index(drop=True)
        filepath = os.path.join(app.config['FILTER_FOLDER'], (file_name + ".csv"))
        df.to_csv(filepath)
        print(df)
        return jsonify({"filtered_data": df.to_json()})
    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == '__main__':
    app.run()
