from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from config.database import Base


class StatusPengiriman(Base):
    __tablename__ = "status_pengiriman"

    id = Column(Integer, primary_key=True, index=True)
    nama_status = Column(String(50))  # contoh: menunggu, dikirim, selesai, dibatalkan

    pesanan_list = relationship("Pesanan", back_populates="status_pengiriman")
