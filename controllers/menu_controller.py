from flask import jsonify, request
from sqlalchemy.orm import Session
from datetime import datetime
from config.database import get_db
from models.menu_model import Menu


def get_semua_menu():
    db: Session = next(get_db())
    data = db.query(Menu).all()
    return jsonify([
        {
            "id": m.id,
            "kategori_id": m.kategori_id,
            "nama": m.nama,
            "harga": float(m.harga),
            "deskripsi": m.deskripsi,
            "gambar_url": m.gambar_url,
        } for m in data
    ])


def tambah_menu():
    db: Session = next(get_db())
    body = request.json

    menu = Menu(
        kategori_id=body["kategori_id"],
        nama=body["nama"],
        deskripsi=body.get("deskripsi"),
        harga=body["harga"],
        gambar_url=body.get("gambar_url")
    )
    db.add(menu)
    db.commit()
    db.refresh(menu)
    return jsonify({"pesan": "Menu berhasil ditambahkan", "id": menu.id})


def ubah_menu(id_menu):
    db: Session = next(get_db())
    body = request.json
    menu = db.query(Menu).filter(Menu.id == id_menu).first()
    if not menu:
        return jsonify({"kesalahan": "Menu tidak ditemukan"}), 404

    for k, v in body.items():
        setattr(menu, k, v)
    menu.diperbarui_pada = datetime.utcnow()
    db.commit()
    return jsonify({"pesan": "Menu berhasil diperbarui"})


def hapus_menu(id_menu):
    db: Session = next(get_db())
    menu = db.query(Menu).filter(Menu.id == id_menu).first()
    if not menu:
        return jsonify({"kesalahan": "Menu tidak ditemukan"}), 404

    db.delete(menu)
    db.commit()
    return jsonify({"pesan": "Menu berhasil dihapus"})
