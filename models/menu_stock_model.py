from sqlalchemy import Column, Integer, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base
from datetime import datetime


class StokMenu(Base):
    __tablename__ = "stok_menu"

    id = Column(Integer, primary_key=True, index=True)
    menu_id = Column(Integer, ForeignKey("menu.id"), nullable=False)
    jumlah = Column(Integer, nullable=False)
    tanggal_stok = Column(Date, nullable=False)
    dibuat_pada = Column(DateTime, default=datetime.utcnow)
    diperbarui_pada = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    menu = relationship("Menu", back_populates="stok_list")
