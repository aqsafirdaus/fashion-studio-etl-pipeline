import pandas as pd

def transform_data(raw_data):
    try:
        df = pd.DataFrame(raw_data)

        dirty_patterns = {
            "Title": ["Unknown Product"], 
            "Rating": ["Invalid Rating / 5", "Not Rated"],
            "Price": ["Price Unavailable", None]
        }

        df = df[~df["Title"].isin(dirty_patterns["Title"])]
        df = df[~df["Rating"].isin(dirty_patterns["Rating"])]
        df = df[~df["Price"].isin(dirty_patterns["Price"])]

        # CLEAN TITLE
        df["Title"] = (df["Title"].astype(object))

        # CLEAN PRICE "$120.50" → 120.50
        df["Price"] = ( df["Price"].replace(r'[\$,]', '', regex=True).astype(float))

        # CONVERT USD → RUPIAH
        df["Price"] = df["Price"] * 16000

        # CLEAN RATING "4.8 / 5" → 4.8
        df["Rating"] = (df["Rating"].str.extract(r'(\d+\.\d+)').astype(float))

        # CLEAN COLORS "3 Colors" → 3
        df["Colors"] = (df["Colors"].str.extract(r'(\d+)').astype(int))

        # CLEAN SIZE
        df["Size"] = (df["Size"].str.replace("Size:", "", regex=False).str.strip().astype(object))

        # CLEAN GENDER
        df["Gender"] = (df["Gender"].str.replace("Gender:", "", regex=False).str.strip().astype(object))

        # CLEAN TIMESTAMP
        df["Timestamp"] = pd.to_datetime(df["Timestamp"])

        # REMOVE DUPLICATES
        df = df.drop_duplicates()

        # REMOVE NULL
        df = df.dropna()

        # RESET INDEX
        df = df.reset_index(drop=True)

        return df

    except KeyError as e:
        print(f"Column not found: {e}")
        return None

    except Exception as e:
        print(f"Error during transformation: {e}")
        return None