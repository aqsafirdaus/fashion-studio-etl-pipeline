import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime

BASE_URL = "https://fashion-studio.dicoding.dev"

headers = {
    "User-Agent": "Mozilla/5.0"
}

def extract_data():

    all_products = []

    try:
        # looping halaman
        for page in range(1, 51):

            if page == 1:
                url = BASE_URL
            else:
                url = f"{BASE_URL}/page{page}"

            print(f"Scraping: {url}")

            response = requests.get(url, headers=headers)

            # skip jika gagal
            if response.status_code != 200:
                print("Halaman gagal diakses")
                continue

            soup = BeautifulSoup(response.text, "html.parser")

            # ambil semua card produk
            products = soup.find_all("div", class_="collection-card")

            # stop jika halaman kosong
            if len(products) == 0:
                break

            for product in products:
                try:
                    # TITLE
                    title = product.find("h3")
                    title = title.text.strip() if title else "Unknown"

                    # PRICE
                    price = product.find("span", class_="price")
                    price = price.text.strip() if price else "Unknown"

                    # RATING
                    rating = product.find("p",string=lambda x: x and "Rating" in x)
                    rating = (rating.text.replace("Rating:", "").strip()if rating else "Unknown")

                    # COLORS
                    colors = product.find("p", string=lambda x: x and "Colors" in x)
                    colors = colors.text.replace("Colors:", "").strip() if colors else "Unknown"

                    # SIZE
                    size = product.find("p", string=lambda x: x and "Size" in x)
                    size = size.text.replace("Size:", "").strip() if size else "Unknown"

                    # GENDER
                    gender = product.find("p", string=lambda x: x and "Gender" in x)
                    gender = gender.text.replace("Gender:", "").strip() if gender else "Unknown"

                    # simpan
                    all_products.append({
                    "Title": title,
                    "Price": price,
                    "Rating": rating,
                    "Colors": colors,
                    "Size": size,
                    "Gender": gender,
                    "Timestamp": datetime.now().isoformat()
                    })

                except Exception as e:
                    print(f"Error parsing product: {e}")

        return all_products
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching website: {e}")
        return None

    except Exception as e:
        print(f"An error occurred during scraping: {e}")
        return None
