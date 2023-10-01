# gsheets.py
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from app import app

class gsheets_api:
    def __init__(self) -> None:
        self.authenticate()

    def authenticate(self):
        # Authenticate with Google Sheets API using credentials
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            app.config['GOOGLE_SHEETS_CREDS'], scope)
        self.gc = gspread.authorize(credentials)

    def open_spreadsheet(self,title):
        spreadsheet = self.gc.open(title)
        return spreadsheet
    
    def create_new_sheet(self,sheet_title):
        # Create a new worksheet with the specified title
        self.gc.add_worksheet(title=sheet_title, rows="100", cols="20")
        return f"Created a new sheet with the title: {sheet_title}"
    
    def import_csv(self, spreadsheet_title, file_path, column_mapping):
        spreadsheet = self.open_spreadsheet(spreadsheet_title)
        worksheet = spreadsheet.get_worksheet(0)  # Change the index as needed

        # Read and process the CSV file
        with open(file_path, 'r') as file:
            lines = file.readlines()

        headers = lines[0].strip().split(',')
        mapped_headers = [column_mapping.get(header, header) for header in headers]

        # Write the mapped headers to the Google Sheet
        worksheet.insert_rows(mapped_headers, 1)

        # Insert the data rows
        for line in lines[1:]:
            data = line.strip().split(',')
            worksheet.append_table(data)

        return f"CSV data imported into '{spreadsheet_title}'"

    def select_columns(self, spreadsheet_title, selected_columns):
        spreadsheet = self.open_spreadsheet(spreadsheet_title)
        worksheet = spreadsheet.get_worksheet(0) 

        # Get all data from the worksheet
        all_data = worksheet.get_all_values()

        # Filter and select specific columns
        selected_data = [[row[i] for i in selected_columns] for row in all_data]

        return selected_data