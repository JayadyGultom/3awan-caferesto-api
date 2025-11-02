from sqlalchemy import Column, Integer, DECIMAL, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base
from datetime import datetime


class Pesanan(Base):
    __tablename__ = "pesanan"

    id = Column(Integer, primary_key=True, index=True)
    pelanggan_id = Column(Integer, ForeignKey("pelanggan.id"), nullable=False)
    status_pembayaran_id = Column(Integer, ForeignKey("status_pembayaran.id"), nullable=False)
    status_pengiriman_id = Column(Integer, ForeignKey("status_pengiriman.id"), nullable=False)
    total = Column(DECIMAL(10, 2))
    tanggal_pesanan = Column(DateTime, nullable=False)
    dibuat_pada = Column(DateTime, default=datetime.utcnow)
    diperbarui_pada = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    pelanggan = relationship("Pelanggan", back_populates="pesanan_list")
    status_pembayaran = relationship("StatusPembayaran", back_populates="pesanan_list")
    status_pengiriman = relationship("StatusPengiriman", back_populates="pesanan_list")
    detail_pesanan_list = relationship("DetailPesanan", back_populates="pesanan", cascade="all, delete")
    pembayaran_list = relationship("Pembayaran", back_populates="pesanan", cascade="all, delete")
