# 📋 Tabel yang Harus Diisi Terlebih Dahulu

Agar aplikasi restoran bisa berjalan dengan baik, ada **3 tabel WAJIB** yang harus diisi terlebih dahulu sebelum aplikasi digunakan.

---

## 1. ⚠️ **status_pembayaran** - WAJIB

**Alasan:** Tabel `pesanan` membutuhkan `status_pembayaran_id` yang NOT NULL. Tanpa data ini, **tidak bisa membuat pesanan baru**.

### Data yang harus diisi:

| id | nama_status |
|----|-------------|
| 1  | Belum Bayar |
| 2  | Menunggu Konfirmasi |
| 3  | Lunas |
| 4  | Dikembalikan |
| 5  | Dibatalkan |

### SQL Insert:
```sql
INSERT INTO status_pembayaran (nama_status) VALUES 
('Belum Bayar'),
('Menunggu Konfirmasi'),
('Lunas'),
('Dikembalikan'),
('Dibatalkan');
```

---

## 2. ⚠️ **status_pengiriman** - WAJIB

**Alasan:** Tabel `pesanan` membutuhkan `status_pengiriman_id` yang NOT NULL. Tanpa data ini, **tidak bisa membuat pesanan baru**.

### Data yang harus diisi:

| id | nama_status |
|----|-------------|
| 1  | Menunggu |
| 2  | Diproses |
| 3  | Dikirim |
| 4  | Selesai |
| 5  | Dibatalkan |

### SQL Insert:
```sql
INSERT INTO status_pengiriman (nama_status) VALUES 
('Menunggu'),
('Diproses'),
('Dikirim'),
('Selesai'),
('Dibatalkan');
```

---

## 3. ⚠️ **kategori** - WAJIB

**Alasan:** Tabel `menu` membutuhkan `kategori_id` yang NOT NULL. Tanpa data ini, **tidak bisa menambahkan menu baru**.

### Data yang harus diisi:

| id | nama | induk_id |
|----|------|----------|
| 1  | Makanan | NULL |
| 2  | Minuman | NULL |
| 3  | Snack | NULL |
| 4  | Dessert | NULL |

### SQL Insert:
```sql
INSERT INTO kategori (nama, induk_id) VALUES 
('Makanan', NULL),
('Minuman', NULL),
('Snack', NULL),
('Dessert', NULL);
```

---

## 📊 Urutan Pengisian

**PENTING:** Isi tabel dalam urutan berikut:

1. ✅ **status_pembayaran** (harus pertama)
2. ✅ **status_pengiriman** (harus kedua)
3. ✅ **kategori** (harus ketiga)

Setelah itu baru bisa:
- Menambahkan menu (butuh kategori)
- Membuat pesanan (butuh status_pembayaran dan status_pengiriman)

---

## ⚠️ Dampak Jika Tidak Diisi

Jika tabel-tabel di atas tidak diisi:

1. ❌ **Tidak bisa membuat pesanan** → Error: Foreign key constraint violation
2. ❌ **Tidak bisa menambahkan menu** → Error: Foreign key constraint violation
3. ❌ **Aplikasi Flutter akan error** → StatusViewModel tidak bisa fetch data
4. ❌ **Checkout akan gagal** → Tidak ada status default untuk pesanan

---

## ✅ Cara Verifikasi

Setelah mengisi data, verifikasi dengan:

1. **Cek Status Pembayaran:**
   ```bash
   GET /status-pembayaran
   ```
   Harus mengembalikan minimal 5 status

2. **Cek Status Pengiriman:**
   ```bash
   GET /status-pengiriman
   ```
   Harus mengembalikan minimal 5 status

3. **Cek Kategori:**
   ```bash
   GET /kategori
   ```
   Harus mengembalikan minimal 4 kategori

---

## 📝 Catatan

- Data di atas adalah **data minimal** yang diperlukan
- Anda bisa menambahkan lebih banyak data sesuai kebutuhan
- Pastikan ID dimulai dari 1 (auto-increment)
- Untuk production, pastikan semua data sudah diisi sebelum deploy




