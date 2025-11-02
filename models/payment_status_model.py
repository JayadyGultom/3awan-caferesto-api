from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from config.database import Base


class StatusPembayaran(Base):
    __tablename__ = "status_pembayaran"

    id = Column(Integer, primary_key=True, index=True)
    nama_status = Column(String(50))  # contoh: lunas, belum_bayar, dikembalikan

    pesanan_list = relationship("Pesanan", back_populates="status_pembayaran")
