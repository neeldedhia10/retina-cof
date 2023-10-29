import os
import csv
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# Set up the Google Drive API
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
creds = None

# The token.json file should be generated when you set up API credentials
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)

if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)

    with open('token.json', 'w') as token:
        token.write(creds.to_json())

# Initialize the Google Drive API
drive_service = build('drive', 'v3', credentials=creds)

# ID of the main Google Drive folder containing subfolders
main_folder_id = '1yyT2KWBNFFmV2nOq1b1B5oXPR6XTVKne'

# Initialize variables for pagination
page_token = None
all_files = []

# Function to retrieve files in a folder
def list_files_in_folder(folder_id):
    folder_files = []
    page_token = None
    while True:
        results = drive_service.files().list(
            q=f"'{folder_id}' in parents and mimeType contains 'image/'",
            fields="files(id, name, webViewLink), nextPageToken",
            pageToken=page_token).execute()

        files = results.get('files', [])
        folder_files.extend(files)

        page_token = results.get('nextPageToken')
        if not page_token:
            break
    return folder_files

# Retrieve the list of subfolders in the main folder
subfolders = drive_service.files().list(
    q=f"'{main_folder_id}' in parents and mimeType = 'application/vnd.google-apps.folder'",
    fields="files(id, name)").execute()
subfolder_ids = [subfolder['id'] for subfolder in subfolders.get('files', [])]

# Loop through the subfolders and retrieve their files
for subfolder_id in subfolder_ids:
    subfolder_files = list_files_in_folder(subfolder_id)
    all_files.extend(subfolder_files)

# Write file names and sharing links to a CSV file
with open('image_links.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['File Name', 'Sharing Link'])

    for file in all_files:
        file_name = file['name']
        file_id = file['id']
        csvwriter.writerow([file_name, file_id])

print("CSV file created successfully.")
