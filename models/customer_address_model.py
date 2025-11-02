from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base
from datetime import datetime


class AlamatPelanggan(Base):
    __tablename__ = "alamat_pelanggan"

    id = Column(Integer, primary_key=True, index=True)
    pelanggan_id = Column(Integer, ForeignKey("pelanggan.id"), nullable=False)
    alamat = Column(String(255))
    utama = Column(Boolean, default=False)
    dibuat_pada = Column(DateTime, default=datetime.utcnow)
    diperbarui_pada = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    pelanggan = relationship("Pelanggan", back_populates="alamat_list")
