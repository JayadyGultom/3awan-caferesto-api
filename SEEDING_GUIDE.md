# 📋 Panduan Seeding Data Awal

## 🎯 Tabel yang HARUS Diisi Terlebih Dahulu

Agar aplikasi restoran bisa berjalan dengan baik, ada beberapa tabel yang **WAJIB** diisi terlebih dahulu sebelum aplikasi digunakan:

### 1. ⚠️ **status_pembayaran** - WAJIB
**Alasan:** 
- Tabel `pesanan` memiliki foreign key `status_pembayaran_id` yang **NOT NULL**
- Aplikasi Flutter membutuhkan data ini untuk membuat pesanan
- Tanpa data ini, **tidak bisa membuat pesanan baru**

**Data yang akan di-seed:**
- Belum Bayar
- Menunggu Konfirmasi
- Lunas
- Dikembalikan
- Dibatalkan

### 2. ⚠️ **status_pengiriman** - WAJIB
**Alasan:**
- Tabel `pesanan` memiliki foreign key `status_pengiriman_id` yang **NOT NULL**
- Aplikasi Flutter membutuhkan data ini untuk membuat pesanan
- Tanpa data ini, **tidak bisa membuat pesanan baru**

**Data yang akan di-seed:**
- Menunggu
- Diproses
- Dikirim
- Selesai
- Dibatalkan

### 3. ⚠️ **kategori** - WAJIB
**Alasan:**
- Tabel `menu` memiliki foreign key `kategori_id` yang **NOT NULL**
- Tanpa kategori, **tidak bisa menambahkan menu baru**

**Data yang akan di-seed:**
- Makanan
- Minuman
- Snack
- Dessert

## 🚀 Cara Menjalankan Seeding

### Opsi 1: Manual (Disarankan)
Jalankan script seeding secara manual:

```bash
cd 3awan-caferesto-api
python seed_data.py
```

### Opsi 2: Otomatis saat Startup
Script seeding sudah diintegrasikan di `app.py` dan akan otomatis dijalankan saat aplikasi pertama kali di-start (jika belum ada data).

## ✅ Verifikasi Seeding Berhasil

Setelah menjalankan seeding, pastikan data sudah ada:

1. **Cek Status Pembayaran:**
   ```bash
   curl http://localhost:5000/status-pembayaran
   ```
   Harus mengembalikan minimal 5 status

2. **Cek Status Pengiriman:**
   ```bash
   curl http://localhost:5000/status-pengiriman
   ```
   Harus mengembalikan minimal 5 status

3. **Cek Kategori:**
   ```bash
   curl http://localhost:5000/kategori
   ```
   Harus mengembalikan minimal 4 kategori

## 🔄 Relasi Tabel

```
pesanan
  ├── status_pembayaran_id → status_pembayaran.id (WAJIB)
  ├── status_pengiriman_id → status_pengiriman.id (WAJIB)
  └── pelanggan_id → pelanggan.id

menu
  └── kategori_id → kategori.id (WAJIB)
```

## ⚠️ Dampak Jika Tidak Di-Seed

Jika tabel-tabel di atas tidak diisi:

1. ❌ **Tidak bisa membuat pesanan** - Error foreign key constraint
2. ❌ **Tidak bisa menambahkan menu** - Error foreign key constraint
3. ❌ **Aplikasi Flutter akan error** - StatusViewModel tidak bisa fetch data
4. ❌ **Checkout akan gagal** - Tidak ada status default untuk pesanan

## 📝 Catatan

- Script seeding **aman dijalankan berkali-kali** - akan skip jika data sudah ada
- Data yang di-seed adalah data dasar, bisa ditambah manual melalui API
- Untuk production, pastikan semua data sudah di-seed sebelum deploy




