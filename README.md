# Fashion Studio ETL Pipeline: Web Scraping, Data Transformation, and Multi-Destination Data Loading

## Deskripsi Proyek

Proyek ini merupakan implementasi **ETL (Extract, Transform, Load) Pipeline** untuk mengumpulkan data produk dari website kompetitor Fashion Studio.

Website sumber data:

https://fashion-studio.dicoding.dev

Data yang diambil meliputi:

* Title
* Price
* Rating
* Colors
* Size
* Gender
* Timestamp

Pipeline ini bertujuan untuk membantu tim Data Science memperoleh data kompetitor yang telah dibersihkan dan siap digunakan untuk analisis bisnis maupun pengembangan model machine learning.

---

# Arsitektur ETL

```text
Fashion Studio Website
           │
           ▼
      EXTRACT
           │
           ▼
      TRANSFORM
           │
           ▼
         LOAD
      ┌────┼────┐
      ▼    ▼    ▼
    CSV  Google PostgreSQL
          Sheets
```

---

# Struktur Project

```text
submission/
│
├── main.py
│
├── utils/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── tests/
│   ├── test_extract.py
│   ├── test_transform.py
│   └── test_load.py
│
├── requirements.txt
│
├── google-sheets-api.json
│
└── README.md
```

---

# Tahapan ETL

## 1. Extract

Tahap extract digunakan untuk mengambil data produk dari website Fashion Studio menggunakan:

* Requests
* BeautifulSoup

Data diambil dari seluruh halaman website mulai dari halaman 1 sampai halaman 50.

### Data yang diekstrak

| Kolom     | Deskripsi             |
| --------- | --------------------- |
| Title     | Nama produk           |
| Price     | Harga produk          |
| Rating    | Rating produk         |
| Colors    | Jumlah warna tersedia |
| Size      | Ukuran produk         |
| Gender    | Target gender         |
| Timestamp | Waktu scraping        |

### Fitur Extract

* Melakukan scraping multi-page
* Menggunakan User-Agent
* Error handling
* Stop otomatis jika halaman kosong
* Menyimpan timestamp scraping

---

## 2. Transform

Tahap transform digunakan untuk membersihkan dan mempersiapkan data sebelum disimpan.

### Proses Transformasi

#### Menghapus Data Tidak Valid

Data berikut akan dihapus:

**Title**

```text
Unknown Product
```

**Rating**

```text
Invalid Rating / 5
Not Rated
```

**Price**

```text
Price Unavailable
```

---

#### Membersihkan Price

Sebelum:

```text
$100
```

Sesudah:

```text
100.0
```

Kemudian dikonversi ke Rupiah:

```text
100 × 16000 = 1.600.000
```

---

#### Membersihkan Rating

Sebelum:

```text
4.8 / 5
```

Sesudah:

```text
4.8
```

---

#### Membersihkan Colors

Sebelum:

```text
3 Colors
```

Sesudah:

```text
3
```

---

#### Konversi Timestamp

Sebelum:

```text
2025-01-01T10:00:00
```

Sesudah:

```python
datetime64[ns]
```

---

#### Data Cleaning Tambahan

* Remove duplicates
* Remove null values
* Reset index

---

## 3. Load

Data yang telah bersih disimpan ke tiga tujuan penyimpanan.

### CSV

Output:

```text
product.csv
```

Menggunakan:

```python
DataFrame.to_csv()
```

---

### Google Sheets

Data diunggah ke Google Sheets menggunakan:

* Google Service Account
* Google Sheets API

Spreadsheet ID:

```text
1SuAwq1qYeIs3f55Vp4Yffj-TixTk1NXidr-irEWYVb4
```

Link Spreadsheet:

https://docs.google.com/spreadsheets/d/1SuAwq1qYeIs3f55Vp4Yffj-TixTk1NXidr-irEWYVb4/edit?gid=0#gid=0

---

### PostgreSQL

Database:

```text
fashiondb
```

Table:

```text
products
```

Connection:

```python
postgresql://developer:supersecretpassword@localhost:5432/fashiondb
```

Data disimpan menggunakan:

```python
DataFrame.to_sql()
```

---

# Teknologi yang Digunakan

| Library                  | Fungsi                |
| ------------------------ | --------------------- |
| pandas                   | Data processing       |
| requests                 | Mengambil halaman web |
| beautifulsoup4           | Parsing HTML          |
| sqlalchemy               | Koneksi PostgreSQL    |
| psycopg2                 | Driver PostgreSQL     |
| google-auth              | Autentikasi Google    |
| google-api-python-client | Google Sheets API     |
| pytest                   | Unit Testing          |
| coverage                 | Test Coverage         |

---

# Instalasi

Clone repository:

```bash
git clone <repository-url>
cd submission
```

Install dependency:

```bash
pip install -r requirements.txt
```

---

# Menjalankan ETL Pipeline

```bash
python main.py
```

Output:

```text
CSV saved!
Google Sheets saved!
PostgreSQL saved!
```

---

# Menjalankan Unit Test

Menjalankan seluruh test:

```bash
python -m pytest tests
```

atau

```bash
pytest tests
```

---

# Menjalankan Test Coverage

```bash
pytest --cov=utils --cov-report=term-missing tests/
```

Contoh output:

```text
---------- coverage ----------
Name                Stmts   Miss Cover
---------------------------------------
extract.py             50      2   96%
transform.py           40      0  100%
load.py                45      1   98%
---------------------------------------
TOTAL                 135      3   98%
```

---

# Unit Testing

## Test Extract

Pengujian meliputi:

* Extract tidak menghasilkan None
* Return berupa list
* Data berhasil diambil
* Request exception handling
* Validasi key hasil scraping

File:

```text
tests/test_extract.py
```

---

## Test Transform

Pengujian meliputi:

* Return DataFrame
* Price bertipe float
* Rating bertipe float
* Colors bertipe integer
* Handling input None
* Handling data kosong
* Penghapusan data invalid

File:

```text
tests/test_transform.py
```

---

## Test Load

Pengujian meliputi:

* Penyimpanan CSV
* Error handling CSV
* Upload Google Sheets
* Penyimpanan PostgreSQL

File:

```text
tests/test_load.py
```

---

# Output Dataset

Dataset akhir memiliki struktur berikut:

| Kolom     | Tipe Data |
| --------- | --------- |
| Title     | object    |
| Price     | float     |
| Rating    | float     |
| Colors    | int       |
| Size      | object    |
| Gender    | object    |
| Timestamp | datetime  |

---

# Hasil Akhir

Pipeline ETL berhasil:

✔ Mengambil data produk Fashion Studio

✔ Membersihkan data yang tidak valid

✔ Mengonversi harga USD ke Rupiah

✔ Menghapus data duplikat dan null

✔ Menyimpan data ke CSV

✔ Menyimpan data ke Google Sheets

✔ Menyimpan data ke PostgreSQL

✔ Memiliki unit testing menggunakan Pytest

✔ Mendukung pengujian coverage menggunakan pytest-cov
