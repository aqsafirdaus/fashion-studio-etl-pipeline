from utils.extract import extract_data
from utils.transform import transform_data
from utils.load import save_to_csv
from utils.load import save_to_google_sheets
from utils.load import save_to_postgresql

def main():
    try:
        # EXTRACT
        print("Starting Extract Process...")
        raw_data = extract_data()

        if raw_data is None:
            print("Extract failed!")
            return

        print("Extract success!")

        # TRANSFORM
        print("Starting Transform Process...")
        clean_df = transform_data(raw_data)

        if clean_df is None:
            print("Transform failed!")
            return

        print("Transform success!")

        # LOAD CSV
        print("Saving to CSV...")
        save_to_csv(clean_df)

        # LOAD GOOGLE SHEETS
        print("Saving to Google Sheets...")
        save_to_google_sheets(clean_df)

        # LOAD POSTGRESQL
        print("Saving to PostgreSQL...")
        save_to_postgresql(clean_df)

        print("ETL Pipeline Success!")

    except Exception as e:
        print(f"Main Pipeline Error: {e}")

if __name__ == "__main__":
    main()