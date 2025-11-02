from sqlalchemy import Column, Integer, String, DECIMAL, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base
from datetime import datetime


class Pembayaran(Base):
    __tablename__ = "pembayaran"

    id = Column(Integer, primary_key=True, index=True)
    pesanan_id = Column(Integer, ForeignKey("pesanan.id"), nullable=False)
    metode = Column(String(50))  # tunai, qris, kartu, transfer
    jumlah = Column(DECIMAL(10, 2))
    tanggal_bayar = Column(DateTime)
    dibuat_pada = Column(DateTime, default=datetime.utcnow)
    diperbarui_pada = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    pesanan = relationship("Pesanan", back_populates="pembayaran_list")
