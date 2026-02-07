import os
from datetime import datetime
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

SPREADSHEET_ID = "180PzOZLjUsxHGGHNGJwCJEU4UFcNU3CQR_pUGs9Hc48"
SHEET_NAME = "Sheet1"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CREDENTIALS_PATH = os.path.join(BASE_DIR, "credentials.json")

def append_to_sheet(data: dict):
    print("🧾 DATA RECEIVED FOR SHEET:", data)

    creds = Credentials.from_service_account_file(
        CREDENTIALS_PATH,
        scopes=["https://www.googleapis.com/auth/spreadsheets"]
    )

    service = build("sheets", "v4", credentials=creds)

    row = [
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        data.get("Organization Name") or "",
        data.get("Person Name") or "",
        data.get("Contact Number") or "",
        data.get("Email ID") or "",
        data.get("Website") or "",
        data.get("Address") or "",
    ]

    print("➡️ ROW INSERTED:", row)

    service.spreadsheets().values().append(
        spreadsheetId=SPREADSHEET_ID,
        range=SHEET_NAME,
        valueInputOption="RAW",
        insertDataOption="INSERT_ROWS",
        body={"values": [row]}
    ).execute()

    print("✅ Google Sheet Updated")
