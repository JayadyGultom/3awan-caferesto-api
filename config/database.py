import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Ambil URL dari environment Railway, atau fallback ke lokal
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:HXDfPtEnAQUAvkyiiKLSFpzhlMwHmGAP@ballast.proxy.rlwy.net:43287/railway"
)

# Tambahkan SSL mode agar aman di Railway
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://")

# Engine koneksi
engine = create_engine(DATABASE_URL, connect_args={"sslmode": "require"}, echo=True)

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
