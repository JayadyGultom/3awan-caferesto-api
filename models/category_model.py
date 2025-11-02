from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base
from datetime import datetime


class Kategori(Base):
    __tablename__ = "kategori"

    id = Column(Integer, primary_key=True, index=True)
    nama = Column(String(100), nullable=False)
    induk_id = Column(Integer, ForeignKey("kategori.id"), nullable=True)
    dibuat_pada = Column(DateTime, default=datetime.utcnow)
    diperbarui_pada = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    induk = relationship("Kategori", remote_side=[id], backref="subkategori")
    menu_list = relationship("Menu", back_populates="kategori")
