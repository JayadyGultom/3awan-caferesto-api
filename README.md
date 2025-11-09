# 🍽️ 3awan Caferesto - Backend API

## 📚 Tentang Proyek

Proyek ini merupakan **tugas kuliah Mobile Programming** untuk membuat aplikasi mobile **"3awan Caferesto"** - sebuah aplikasi restoran/kafe yang memungkinkan pelanggan untuk memesan makanan dan minuman secara online.

### 🎯 Stack Teknologi

- **Frontend Mobile**: Flutter
- **Backend API**: Python (Flask)
- **Database**: PostgreSQL (Railway)
- **Hosting**: Railway (Cloud Platform)

---

## 📖 Deskripsi Aplikasi

**3awan Caferesto** adalah aplikasi mobile untuk restoran/kafe yang menyediakan fitur-fitur berikut:

- 📱 **Registrasi & Login** - Autentikasi pengguna (pelanggan/admin)
- 🍕 **Menu Management** - Melihat menu makanan dan minuman
- 🛒 **Shopping Cart** - Keranjang belanja untuk memesan
- 📦 **Order Management** - Mengelola pesanan pelanggan
- 💳 **Payment System** - Sistem pembayaran pesanan
- 🚚 **Delivery Tracking** - Pelacakan status pengiriman
- 📍 **Address Management** - Pengelolaan alamat pengiriman

---

## 📁 Struktur Folder dan Kegunaannya

```
3awan-caferesto-api/
│
├── 📂 config/                    # Konfigurasi aplikasi
│   └── database.py              # Konfigurasi koneksi database PostgreSQL
│
├── 📂 models/                    # Model database (SQLAlchemy ORM)
│   ├── user_account_model.py    # Model untuk akun pengguna
│   ├── customer_model.py        # Model untuk data pelanggan
│   ├── customer_address_model.py # Model untuk alamat pelanggan
│   ├── category_model.py        # Model untuk kategori menu
│   ├── menu_model.py            # Model untuk menu makanan/minuman
│   ├── menu_stock_model.py      # Model untuk stok menu
│   ├── order_model.py           # Model untuk pesanan
│   ├── order_item_model.py      # Model untuk detail item pesanan
│   ├── payment_model.py         # Model untuk pembayaran
│   ├── payment_status_model.py  # Model untuk status pembayaran
│   └── delivery_status_model.py # Model untuk status pengiriman
│
├── 📂 controllers/               # Business logic layer
│   ├── user_account_controller.py    # Controller untuk akun pengguna
│   ├── customer_controller.py        # Controller untuk pelanggan
│   ├── customer_address_controller.py # Controller untuk alamat
│   ├── category_controller.py        # Controller untuk kategori
│   ├── menu_controller.py            # Controller untuk menu
│   ├── menu_stock_controller.py      # Controller untuk stok
│   ├── order_controller.py           # Controller untuk pesanan
│   ├── order_item_controller.py      # Controller untuk detail pesanan
│   ├── payment_controller.py         # Controller untuk pembayaran
│   ├── payment_status_controller.py  # Controller untuk status pembayaran
│   └── delivery_status_controller.py # Controller untuk status pengiriman
│
├── 📂 routes/                    # API endpoints (Flask Blueprint)
│   ├── __init__.py              # Registrasi semua routes
│   ├── user_routes.py           # Routes untuk autentikasi (register/login)
│   ├── customer_routes.py       # Routes untuk CRUD pelanggan
│   ├── customer_address_routes.py # Routes untuk CRUD alamat
│   ├── category_routes.py       # Routes untuk CRUD kategori
│   ├── menu_routes.py           # Routes untuk CRUD menu
│   ├── menu_stock_routes.py     # Routes untuk CRUD stok
│   ├── order_routes.py          # Routes untuk CRUD pesanan
│   ├── order_item_routes.py     # Routes untuk CRUD detail pesanan
│   ├── payment_routes.py        # Routes untuk CRUD pembayaran
│   ├── payment_status_routes.py # Routes untuk CRUD status pembayaran
│   └── delivery_status_routes.py # Routes untuk CRUD status pengiriman
│
├── 📄 app.py                     # File utama aplikasi Flask
├── 📄 requirements.txt           # Dependencies Python
├── 📄 README.md                  # Dokumentasi proyek (file ini)
├── 📄 DATA_YANG_HARUS_DIISI.md   # Panduan data awal yang harus diisi
├── 📄 README_SEEDING.md          # Panduan seeding database
└── 📄 SEEDING_GUIDE.md           # Panduan lengkap seeding
```

### 🔍 Penjelasan Struktur:

1. **`config/`** - Berisi konfigurasi database dan koneksi ke PostgreSQL Railway
2. **`models/`** - Mendefinisikan struktur tabel database menggunakan SQLAlchemy ORM
3. **`controllers/`** - Berisi business logic untuk setiap entitas (CRUD operations)
4. **`routes/`** - Mendefinisikan API endpoints yang dapat diakses oleh aplikasi Flutter
5. **`app.py`** - File utama yang menjalankan server Flask dan mendaftarkan semua routes

---

## 🚀 Proses Pengerjaan

### 1. **Perencanaan (Planning)**
   - Menentukan fitur aplikasi restoran
   - Merancang database schema (11 tabel dengan relasi)
   - Merencanakan API endpoints yang dibutuhkan

### 2. **Database Design**
   - Membuat 11 tabel dengan relasi foreign key:
     - `pengguna` - Akun pengguna (login/register)
     - `pelanggan` - Data pelanggan
     - `alamat_pelanggan` - Alamat pengiriman
     - `kategori` - Kategori menu (Makanan, Minuman, dll)
     - `menu` - Menu makanan/minuman
     - `stok_menu` - Stok menu
     - `pesanan` - Pesanan pelanggan
     - `detail_pesanan` - Item-item dalam pesanan
     - `pembayaran` - Data pembayaran
     - `status_pembayaran` - Status pembayaran (Belum Bayar, Lunas, dll)
     - `status_pengiriman` - Status pengiriman (Menunggu, Dikirim, Selesai, dll)

### 3. **Backend Development**
   - Setup Flask application dengan SQLAlchemy ORM
   - Membuat models untuk setiap tabel
   - Membuat controllers untuk business logic
   - Membuat routes/endpoints untuk API
   - Implementasi CORS untuk akses dari Flutter

### 4. **Database Setup**
   - Setup PostgreSQL database di Railway
   - Konfigurasi koneksi database
   - Auto-create tables saat aplikasi dijalankan
   - Seeding data awal (status pembayaran, status pengiriman, kategori)

### 5. **API Testing**
   - Testing semua endpoints dengan Postman/Insomnia
   - Verifikasi CRUD operations
   - Testing autentikasi (register/login)

### 6. **Deployment**
   - Deploy ke Railway
   - Konfigurasi environment variables
   - Testing API di production

### 7. **Integration dengan Flutter**
   - Flutter app mengonsumsi API endpoints
   - Implementasi HTTP requests dari Flutter
   - Testing integrasi frontend-backend

---

## 🛠️ Cara Menggunakan Code dari GitHub

### Prerequisites

Sebelum mulai, pastikan Anda sudah menginstall:
- **Python 3.8+** 
- **PostgreSQL** (atau gunakan Railway PostgreSQL)
- **pip** (Python package manager)
- **Git** (untuk clone repository)

### Langkah 1: Clone Repository

```bash
git clone <url-repository-github>
cd 3awan-caferesto-api
```

### Langkah 2: Setup Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Langkah 3: Install Dependencies

```bash
pip install -r requirements.txt
```

Dependencies yang akan diinstall:
- `Flask==3.0.0` - Web framework
- `SQLAlchemy==2.0.36` - ORM untuk database
- `psycopg2-binary` - PostgreSQL adapter
- `flask-cors` - CORS support untuk Flutter

### Langkah 4: Konfigurasi Database

#### Opsi A: Menggunakan Railway PostgreSQL (Recommended)

1. Buat akun di [Railway](https://railway.app)
2. Buat PostgreSQL database baru
3. Copy connection string dari Railway
4. Update file `config/database.py` atau set environment variable:

```bash
# Windows PowerShell
$env:DATABASE_URL="postgresql://user:password@host:port/database"

# Linux/Mac
export DATABASE_URL="postgresql://user:password@host:port/database"
```

#### Opsi B: Menggunakan PostgreSQL Lokal

1. Install PostgreSQL di komputer Anda
2. Buat database baru:
```sql
CREATE DATABASE caferesto_db;
```
3. Update `config/database.py` dengan connection string lokal:
```python
DATABASE_URL = "postgresql://username:password@localhost:5432/caferesto_db"
```

### Langkah 5: Jalankan Aplikasi

```bash
python app.py
```

Server akan berjalan di `http://localhost:5000`

### Langkah 6: Setup Data Awal (Seeding)

**PENTING:** Sebelum menggunakan aplikasi, Anda harus mengisi 3 tabel berikut:

1. **status_pembayaran** - Status pembayaran (Belum Bayar, Lunas, dll)
2. **status_pengiriman** - Status pengiriman (Menunggu, Dikirim, Selesai, dll)
3. **kategori** - Kategori menu (Makanan, Minuman, Snack, Dessert)

**Cara 1: Menggunakan API Endpoints**

```bash
# Tambah status pembayaran
POST http://localhost:5000/status-pembayaran
{
  "nama_status": "Belum Bayar"
}

# Tambah status pengiriman
POST http://localhost:5000/status-pengiriman
{
  "nama_status": "Menunggu"
}

# Tambah kategori
POST http://localhost:5000/kategori
{
  "nama": "Makanan",
  "induk_id": null
}
```

**Cara 2: Menggunakan SQL langsung**

Lihat file `DATA_YANG_HARUS_DIISI.md` untuk SQL insert statements.

### Langkah 7: Testing API

Gunakan Postman atau Insomnia untuk test API endpoints:

```bash
# Test home endpoint
GET http://localhost:5000/

# Test register user
POST http://localhost:5000/pengguna/register
Content-Type: application/json
{
  "email": "test@example.com",
  "sandi_hash": "password123",
  "peran": "pelanggan"
}

# Test login
POST http://localhost:5000/pengguna/login
Content-Type: application/json
{
  "email": "test@example.com",
  "sandi_hash": "password123"
}
```

---

## 📡 API Endpoints

### Autentikasi
- `POST /pengguna/register` - Registrasi pengguna baru
- `POST /pengguna/login` - Login pengguna

### Pelanggan
- `GET /pelanggan` - Ambil semua pelanggan
- `GET /pelanggan/{id}` - Ambil pelanggan by ID
- `POST /pelanggan` - Tambah pelanggan baru
- `PUT /pelanggan/{id}` - Update pelanggan
- `DELETE /pelanggan/{id}` - Hapus pelanggan

### Alamat Pelanggan
- `GET /alamat` - Ambil semua alamat
- `GET /alamat/{id}` - Ambil alamat by ID
- `POST /alamat` - Tambah alamat baru
- `PUT /alamat/{id}` - Update alamat
- `DELETE /alamat/{id}` - Hapus alamat

### Kategori
- `GET /kategori` - Ambil semua kategori
- `GET /kategori/{id}` - Ambil kategori by ID
- `POST /kategori` - Tambah kategori baru
- `PUT /kategori/{id}` - Update kategori
- `DELETE /kategori/{id}` - Hapus kategori

### Menu
- `GET /menu` - Ambil semua menu
- `GET /menu/{id}` - Ambil menu by ID
- `POST /menu` - Tambah menu baru
- `PUT /menu/{id}` - Update menu
- `DELETE /menu/{id}` - Hapus menu

### Pesanan
- `GET /pesanan` - Ambil semua pesanan
- `GET /pesanan/{id}` - Ambil pesanan by ID
- `POST /pesanan` - Tambah pesanan baru
- `PUT /pesanan/{id}` - Update pesanan
- `DELETE /pesanan/{id}` - Hapus pesanan

### Pembayaran
- `GET /pembayaran` - Ambil semua pembayaran
- `GET /pembayaran/{id}` - Ambil pembayaran by ID
- `POST /pembayaran` - Tambah pembayaran baru
- `PUT /pembayaran/{id}` - Update pembayaran
- `DELETE /pembayaran/{id}` - Hapus pembayaran

**Dan banyak lagi...** (Lihat folder `routes/` untuk semua endpoints)

---

## 🌐 Deploy ke Railway

### Langkah 1: Buat Railway Account
1. Kunjungi [Railway](https://railway.app)
2. Sign up dengan GitHub account

### Langkah 2: Buat New Project
1. Klik "New Project"
2. Pilih "Deploy from GitHub repo"
3. Pilih repository ini

### Langkah 3: Setup PostgreSQL Database
1. Di Railway dashboard, klik "New" → "Database" → "PostgreSQL"
2. Railway akan membuat database PostgreSQL secara otomatis
3. Copy connection string dari database settings

### Langkah 4: Setup Environment Variables
1. Di Railway project settings, tambahkan environment variable:
   - `DATABASE_URL` = connection string dari PostgreSQL

### Langkah 5: Deploy
1. Railway akan otomatis deploy saat ada push ke GitHub
2. Atau klik "Deploy" manual di dashboard
3. Tunggu hingga deployment selesai
4. Copy URL API dari Railway (contoh: `https://your-app.railway.app`)

### Langkah 6: Update Flutter App
Update base URL di aplikasi Flutter ke URL Railway:
```dart
final String baseUrl = "https://your-app.railway.app";
```

---

## 📝 Catatan Penting

1. **Database Seeding**: Pastikan mengisi data awal (status pembayaran, status pengiriman, kategori) sebelum menggunakan aplikasi
2. **CORS**: API sudah dikonfigurasi untuk menerima request dari Flutter (CORS enabled)
3. **Password Hashing**: Password di-hash menggunakan Werkzeug sebelum disimpan di database
4. **Database Migration**: Tables akan otomatis dibuat saat aplikasi pertama kali dijalankan
5. **Environment Variables**: Gunakan environment variables untuk sensitive data (database URL, API keys, dll)

---

## 🐛 Troubleshooting

### Error: "Could not connect to database"
- Pastikan PostgreSQL database sudah running
- Cek connection string di `config/database.py`
- Pastikan environment variable `DATABASE_URL` sudah di-set

### Error: "Table does not exist"
- Pastikan aplikasi sudah dijalankan setidaknya sekali untuk create tables
- Cek apakah `Base.metadata.create_all(bind=engine)` sudah dijalankan di `app.py`

### Error: "Foreign key constraint violation"
- Pastikan data referensi sudah ada (contoh: kategori sebelum menu, status sebelum pesanan)
- Lihat `DATA_YANG_HARUS_DIISI.md` untuk urutan pengisian data

### Error: "CORS policy"
- Pastikan `flask-cors` sudah diinstall
- Pastikan `CORS(app)` sudah dikonfigurasi di `app.py`

---

## 📚 Dokumentasi Tambahan

- `DATA_YANG_HARUS_DIISI.md` - Panduan data awal yang harus diisi
- `README_SEEDING.md` - Panduan seeding database
- `SEEDING_GUIDE.md` - Panduan lengkap seeding

---

## 👨‍💻 Developer

**Nama**: Jayady Managam Gultom  
**NIM**: 12523027  
**Mata Kuliah**: Mobile Programming  
**Proyek**: 3awan Caferesto - Aplikasi Restoran Mobile

---

## 📄 License

Proyek ini dibuat untuk keperluan tugas kuliah.

---

## 🙏 Acknowledgments

- Flask Framework
- SQLAlchemy ORM
- Railway Platform
- PostgreSQL Database

---

**Happy Coding! 🚀**
