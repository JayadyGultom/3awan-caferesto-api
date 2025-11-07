from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Ambil URL dari Railway
DATABASE_URL = os.getenv("postgresql://postgres:HXDfPtEnAQUAvkyiiKLSFpzhlMwHmGAP@ballast.proxy.rlwy.net:43287/railway")

# Tambahkan sslmode=require jika belum ada
if DATABASE_URL and "sslmode" not in DATABASE_URL:
    DATABASE_URL += "?sslmode=require"

# Buat koneksi
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
