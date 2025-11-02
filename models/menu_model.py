from sqlalchemy import Column, Integer, String, Text, DECIMAL, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base
from datetime import datetime


class Menu(Base):
    __tablename__ = "menu"

    id = Column(Integer, primary_key=True, index=True)
    kategori_id = Column(Integer, ForeignKey("kategori.id"), nullable=False)
    nama = Column(String(100), nullable=False)
    deskripsi = Column(Text)
    harga = Column(DECIMAL(10, 2), nullable=False)
    gambar_url = Column(Text)
    dibuat_pada = Column(DateTime, default=datetime.utcnow)
    diperbarui_pada = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    kategori = relationship("Kategori", back_populates="menu_list")
    stok_list = relationship("StokMenu", back_populates="menu", cascade="all, delete")
    detail_pesanan = relationship("DetailPesanan", back_populates="menu")
