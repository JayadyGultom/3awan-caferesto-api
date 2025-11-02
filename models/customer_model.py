from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base
from datetime import datetime


class Pelanggan(Base):
    __tablename__ = "pelanggan"

    id = Column(Integer, primary_key=True, index=True)
    pengguna_id = Column(Integer, ForeignKey("pengguna.id"), unique=True, nullable=False)
    nama_lengkap = Column(String(100), nullable=False)
    telepon = Column(String(20))
    dibuat_pada = Column(DateTime, default=datetime.utcnow)
    diperbarui_pada = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    pengguna = relationship("Pengguna", back_populates="pelanggan")
    alamat_list = relationship("AlamatPelanggan", back_populates="pelanggan", cascade="all, delete")
    pesanan_list = relationship("Pesanan", back_populates="pelanggan")
