import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Ambil URL dari environment Railway, atau fallback ke lokal
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:fLWFPKGGRuyEcBBaCPsHfBlHAmWxXyhY@yamabiko.proxy.rlwy.net:43616/railway"
)

# Tambahkan SSL mode agar aman di Railway
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://")

# Engine koneksi dengan connection pool settings untuk mencegah timeout
engine = create_engine(
    DATABASE_URL, 
    connect_args={"sslmode": "require"}, 
    echo=True,
    pool_size=10,  # Jumlah koneksi yang di-pool
    max_overflow=20,  # Koneksi tambahan jika pool penuh
    pool_pre_ping=True,  # Cek koneksi sebelum digunakan (mencegah timeout)
    pool_recycle=3600,  # Recycle koneksi setiap 1 jam
    pool_timeout=30  # Timeout saat mengambil koneksi dari pool
)

# Session dan Base ORM
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency untuk session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
