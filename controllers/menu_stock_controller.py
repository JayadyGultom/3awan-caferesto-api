from flask import jsonify, request
from sqlalchemy.orm import Session
from datetime import datetime
from config.database import get_db
from models.menu_stock_model import StokMenu


def get_semua_stok_menu():
    db: Session = next(get_db())
    data = db.query(StokMenu).all()
    return jsonify([
        {
            "id": s.id,
            "menu_id": s.menu_id,
            "jumlah": s.jumlah,
            "tanggal_stok": s.tanggal_stok.strftime("%Y-%m-%d"),
        } for s in data
    ])


def tambah_stok_menu():
    db: Session = next(get_db())
    body = request.json

    stok = StokMenu(
        menu_id=body["menu_id"],
        jumlah=body["jumlah"],
        tanggal_stok=body["tanggal_stok"]
    )
    db.add(stok)
    db.commit()
    db.refresh(stok)
    return jsonify({"pesan": "Stok menu berhasil ditambahkan", "id": stok.id})


def ubah_stok_menu(id_stok):
    db: Session = next(get_db())
    body = request.json
    stok = db.query(StokMenu).filter(StokMenu.id == id_stok).first()
    if not stok:
        return jsonify({"kesalahan": "Stok menu tidak ditemukan"}), 404

    for k, v in body.items():
        setattr(stok, k, v)
    stok.diperbarui_pada = datetime.utcnow()
    db.commit()
    return jsonify({"pesan": "Stok menu berhasil diperbarui"})


def hapus_stok_menu(id_stok):
    db: Session = next(get_db())
    stok = db.query(StokMenu).filter(StokMenu.id == id_stok).first()
    if not stok:
        return jsonify({"kesalahan": "Stok menu tidak ditemukan"}), 404

    db.delete(stok)
    db.commit()
    return jsonify({"pesan": "Stok menu berhasil dihapus"})
