# 🏢 Aplikasi Inventaris Barang Kantor - API Documentation

## 📋 Overview
Aplikasi CRUD lengkap untuk mengelola inventaris barang kantor dengan 6 tabel utama dan relasi yang kompleks.

## 🗄️ Database Schema

### 1. **kategori** - Kategori Barang
- `id` (INT, PK, AUTO_INCREMENT)
- `nama_kategori` (VARCHAR(100), NOT NULL)
- `deskripsi` (TEXT)

### 2. **lokasi** - Lokasi Penyimpanan
- `id` (INT, PK, AUTO_INCREMENT)
- `nama_lokasi` (VARCHAR(100), NOT NULL)
- `lantai` (VARCHAR(20))
- `keterangan` (TEXT)

### 3. **pegawai** - Data Pegawai
- `id` (INT, PK, AUTO_INCREMENT)
- `nama_pegawai` (VARCHAR(100), NOT NULL)
- `jabatan` (VARCHAR(100))
- `departemen` (VARCHAR(100))
- `email` (VARCHAR(100))

### 4. **barang** - Data Barang
- `id` (INT, PK, AUTO_INCREMENT)
- `nama_barang` (VARCHAR(200), NOT NULL)
- `kategori_id` (INT, FK → kategori.id)
- `lokasi_id` (INT, FK → lokasi.id)
- `jumlah` (INT, NOT NULL)
- `kondisi` (VARCHAR(50), NOT NULL)
- `tanggal_masuk` (DATE, NOT NULL)

### 5. **peminjaman** - Data Peminjaman
- `id` (INT, PK, AUTO_INCREMENT)
- `pegawai_id` (INT, FK → pegawai.id)
- `barang_id` (INT, FK → barang.id)
- `tanggal_pinjam` (DATE, NOT NULL)
- `jumlah_pinjam` (INT, NOT NULL)
- `status` (VARCHAR(50), NOT NULL)

### 6. **pengembalian** - Data Pengembalian
- `id` (INT, PK, AUTO_INCREMENT)
- `peminjaman_id` (INT, FK → peminjaman.id)
- `tanggal_kembali` (DATE, NOT NULL)
- `kondisi_setelah` (VARCHAR(50), NOT NULL)
- `catatan` (TEXT)

## 🚀 API Endpoints

### 📁 Kategori
- `GET /kategori` - Ambil semua kategori
- `GET /kategori/{id}` - Ambil kategori by ID
- `POST /kategori` - Tambah kategori baru
- `PUT /kategori/{id}` - Update kategori
- `DELETE /kategori/{id}` - Hapus kategori

### 📍 Lokasi
- `GET /lokasi` - Ambil semua lokasi
- `GET /lokasi/{id}` - Ambil lokasi by ID
- `POST /lokasi` - Tambah lokasi baru
- `PUT /lokasi/{id}` - Update lokasi
- `DELETE /lokasi/{id}` - Hapus lokasi

### 👥 Pegawai
- `GET /pegawai` - Ambil semua pegawai
- `GET /pegawai/{id}` - Ambil pegawai by ID
- `POST /pegawai` - Tambah pegawai baru
- `PUT /pegawai/{id}` - Update pegawai
- `DELETE /pegawai/{id}` - Hapus pegawai

### 📦 Barang
- `GET /barang` - Ambil semua barang
- `GET /barang/{id}` - Ambil barang by ID
- `POST /barang` - Tambah barang baru
- `PUT /barang/{id}` - Update barang
- `DELETE /barang/{id}` - Hapus barang

### 📋 Peminjaman
- `GET /peminjaman` - Ambil semua peminjaman
- `GET /peminjaman/{id}` - Ambil peminjaman by ID
- `POST /peminjaman` - Tambah peminjaman baru
- `PUT /peminjaman/{id}` - Update peminjaman
- `DELETE /peminjaman/{id}` - Hapus peminjaman

### 🔄 Pengembalian
- `GET /pengembalian` - Ambil semua pengembalian
- `GET /pengembalian/{id}` - Ambil pengembalian by ID
- `POST /pengembalian` - Tambah pengembalian baru
- `PUT /pengembalian/{id}` - Update pengembalian
- `DELETE /pengembalian/{id}` - Hapus pengembalian

## 📝 Contoh Request/Response

### POST /kategori
```json
{
  "nama_kategori": "Elektronik",
  "deskripsi": "Barang-barang elektronik kantor"
}
```

### POST /barang
```json
{
  "nama_barang": "Laptop Lenovo",
  "kategori_id": 1,
  "lokasi_id": 1,
  "jumlah": 5,
  "kondisi": "Baik",
  "tanggal_masuk": "2025-09-20"
}
```

### POST /peminjaman
```json
{
  "pegawai_id": 1,
  "barang_id": 1,
  "tanggal_pinjam": "2025-10-01",
  "jumlah_pinjam": 1,
  "status": "dipinjam"
}
```

## 🛠️ Setup & Installation

1. **Install Dependencies:**
   ```bash
   pip install flask sqlalchemy psycopg2-binary
   ```

2. **Database Configuration:**
   - Update `config/database.py` with your PostgreSQL connection string
   - Run `python app.py` to create tables automatically

3. **Run Application:**
   ```bash
   python app.py
   ```
   - Server runs on `http://localhost:5000`

## ✅ Features Implemented

- ✅ Complete CRUD operations for all 6 entities
- ✅ Foreign key relationships properly configured
- ✅ PostgreSQL database with auto-increment sequences
- ✅ RESTful API design
- ✅ JSON request/response format
- ✅ Error handling with proper HTTP status codes
- ✅ Database connection with Railway PostgreSQL

## 🎯 Ready for Production

Aplikasi ini sudah siap untuk:
- Deploy ke Railway
- Integrasi dengan frontend
- Testing dengan Postman/Insomnia
- Dokumentasi API lengkap

**Total Endpoints:** 30 endpoints (5 CRUD operations × 6 entities)
**Database:** PostgreSQL dengan relasi yang kompleks
**Framework:** Flask + SQLAlchemy

