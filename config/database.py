from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# ==============================================================
# 1️⃣ Ambil URL database dari environment Railway
# ==============================================================
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("❌ DATABASE_URL tidak ditemukan di environment Railway!")

# ==============================================================
# 2️⃣ Perbaiki format URL otomatis (Railway kadang pakai 'postgres://' bukan 'postgresql://')
# ==============================================================
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# ==============================================================
# 3️⃣ Tambahkan sslmode=require hanya jika belum ada
# ==============================================================
if "sslmode" not in DATABASE_URL:
    DATABASE_URL += "?sslmode=require"

# ==============================================================
# 4️⃣ Buat koneksi engine SQLAlchemy
# ==============================================================
try:
    engine = create_engine(
        DATABASE_URL,
        pool_pre_ping=True,   # Pastikan koneksi tetap aktif
        pool_size=5,          # Jumlah koneksi aktif
        max_overflow=10,      # Tambahan koneksi jika sibuk
        pool_timeout=30,      # Tunggu 30 detik kalau pool penuh
        pool_recycle=1800,    # Reset koneksi setiap 30 menit
    )
except Exception as e:
    print(f"❌ Gagal membuat koneksi database: {e}")
    raise e

# ==============================================================
# 5️⃣ Session ORM untuk query database
# ==============================================================
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ==============================================================
# 6️⃣ Base class untuk semua model ORM
# ==============================================================
Base = declarative_base()
