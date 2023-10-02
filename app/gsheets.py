# gsheets.py
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build
import io
from googleapiclient.http import MediaIoBaseUpload
from app import app

class gsheets_api:
    def __init__(self) -> None:
        self.init=1
        self.authenticate()
    def initiate(self,name):
        if(self.init==1):
            self.create_new_google_sheet(name)
        self.init=0
    def authenticate(self):
        # Authenticate with Google Sheets API using credentials
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            app.config['SHEETS_JSON'], scope)
        self.gc = gspread.authorize(credentials)
        self.drive_service = build('drive', 'v3', credentials=credentials)
    
    def create_new_google_sheet(self, sheet_title):
        self.spreadsheet=self.gc.create(sheet_title)
        self.worksheet = self.spreadsheet.get_worksheet(0)
        print("created new sheet")
        self.init=0
    def open_worksheet(self,title):
        self.worksheet=self.spreadsheet.worksheet(title)

    def open_spreadsheet(self,title):
        self.spreadsheet = self.gc.open(title)
    def give_email_access(self, email_id, role):
        
        if(role=="read"):
            role="reader"
        if(role=="comment"):
            role="commenter"
        if(role=="write"):
            role="writer"
        self.spreadsheet.share(email_id, perm_type='user', role=role)
        spreadsheet_link = self.spreadsheet.url
        return spreadsheet_link
    def generate_shareable_link_by_role(self,role):
        if(role=="view"):
            role="reader"
        if(role=="edit"):
            role="writer"
        if(role=="comment"):
            role="commenter"
        self.spreadsheet.share('', perm_type='anyone', role=role)
        spreadsheet_link = self.spreadsheet.url
        return spreadsheet_link
    def generate_shareable_link(self):
        
        self.spreadsheet.share('', perm_type='anyone', role='writer')
        spreadsheet_link = self.spreadsheet.url
        return spreadsheet_link
    
    def create_new_worksheet(self,sheet_title):
        self.spreadsheet.add_worksheet(title=sheet_title, rows="100", cols="20")
        self.open_worksheet(sheet_title)
        print(f"Created a new sheet with the title: {sheet_title}")
    
    def import_csv(self, spreadsheet_title, file_path, selected_columns):
        
        # Get the first worksheet (you can adjust the index if needed)
        #worksheet = self.spreadsheet.get_worksheet(0)
        worksheet=self.worksheet
        # Read and process the CSV file
        with open(file_path, 'r') as file:
            lines = file.readlines()

        headers = lines[0].strip().split(',')
        
        # Create a column mapping dictionary for selected columns
        column_mapping = {header: header for header in headers if header in selected_columns}
        print(column_mapping)
        # Write the mapped headers to the Google Sheet
        worksheet.update('A1', [list(column_mapping.values())])

        # Insert the data rows for selected columns
        data_rows = []
        for line in lines[1:]:
            data = line.strip().split(',')
            selected_data = [data[headers.index(col)] for col in column_mapping.keys()]
            data_rows.append(selected_data)
        
        # Append the data to the worksheet
        worksheet.append_rows(data_rows)

        return self.generate_shareable_link()