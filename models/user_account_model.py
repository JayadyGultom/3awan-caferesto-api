from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship
from config.database import Base
from datetime import datetime

class Pengguna(Base):
    __tablename__ = "pengguna"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, nullable=False)
    sandi_hash = Column(String(255), nullable=False)
    peran = Column(String(50), default="pelanggan")
    status = Column(String(50), default="aktif")
    dibuat_pada = Column(TIMESTAMP, default=datetime.utcnow)
    diperbarui_pada = Column(TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)

    # ✅ tambahkan ini dengan indentasi sejajar
    pelanggan = relationship("Pelanggan", back_populates="pengguna", uselist=False)
