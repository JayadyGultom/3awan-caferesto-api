from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from config.database import Base
from datetime import datetime


class Pengguna(Base):
    __tablename__ = "pengguna"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, nullable=False)
    sandi_hash = Column(String(255), nullable=False)
    peran = Column(String(50))  # contoh: pelanggan, admin
    status = Column(String(50))  # aktif, nonaktif
    dibuat_pada = Column(DateTime, default=datetime.utcnow)
    diperbarui_pada = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    pelanggan = relationship("Pelanggan", back_populates="pengguna", uselist=False)
