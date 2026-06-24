import pandas as pd
from sqlalchemy import create_engine
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from sqlalchemy import create_engine

# SAVE CSV
def save_to_csv(df):
    try:
        df.to_csv("product.csv",index=False)
        print("CSV saved!")
    except Exception as e:
        print(f"CSV Error: {e}")

# Konfigurasi google sheets
SERVICE_ACCOUNT_FILE = "google-sheets-api.json" 
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SPREADSHEET_ID = "1SuAwq1qYeIs3f55Vp4Yffj-TixTk1NXidr-irEWYVb4"
RANGE_NAME = "Sheet1!A1"

# SAVE TO GOOGLE SHEETS
def save_to_google_sheets(df):
    try:
        # build service
        credential = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        service = build("sheets", "v4", credentials=credential)
        sheet = service.spreadsheets()

        # convert Timestamp ke string
        if "Timestamp" in df.columns:
            df["Timestamp"] = df["Timestamp"].astype(str)

        # header kolom
        header = df.columns.tolist()
        values = df.values.tolist()
        data = [header] + values
        body = {
            "values": data
        }

        # upload ke spreadsheet
        result = sheet.values().update(
            spreadsheetId=SPREADSHEET_ID,
            range=RANGE_NAME,
            valueInputOption="RAW",
            body=body
        ).execute()

        print("Google Sheets saved!")

    except Exception as e:
        print(f"Google Sheets Error: {e}")

# SAVE POSTGRESQL
def save_to_postgresql(df):
    try:
        engine = create_engine("postgresql://developer:supersecretpassword@localhost:5432/fashiondb")
        df.to_sql("products", engine, if_exists="replace", index=False)
        print("PostgreSQL saved!")

    except Exception as e:
        print(f"PostgreSQL Error: {e}")