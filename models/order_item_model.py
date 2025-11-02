from sqlalchemy import Column, Integer, DECIMAL, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base
from datetime import datetime


class DetailPesanan(Base):
    __tablename__ = "detail_pesanan"

    id = Column(Integer, primary_key=True, index=True)
    pesanan_id = Column(Integer, ForeignKey("pesanan.id"), nullable=False)
    menu_id = Column(Integer, ForeignKey("menu.id"), nullable=False)
    jumlah = Column(Integer, nullable=False)
    harga_saat_pesanan = Column(DECIMAL(10, 2), nullable=False)
    dibuat_pada = Column(DateTime, default=datetime.utcnow)
    diperbarui_pada = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    pesanan = relationship("Pesanan", back_populates="detail_pesanan_list")
    menu = relationship("Menu", back_populates="detail_pesanan")
