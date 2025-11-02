from flask import jsonify, request
from sqlalchemy.orm import Session
from datetime import datetime
from config.database import get_db
from models.category_model import Kategori


def get_semua_kategori():
    db: Session = next(get_db())
    data = db.query(Kategori).all()
    return jsonify([
        {
            "id": k.id,
            "nama": k.nama,
            "induk_id": k.induk_id,
        } for k in data
    ])


def tambah_kategori():
    db: Session = next(get_db())
    body = request.json

    kategori = Kategori(
        nama=body["nama"],
        induk_id=body.get("induk_id"),
    )
    db.add(kategori)
    db.commit()
    db.refresh(kategori)
    return jsonify({"pesan": "Kategori berhasil ditambahkan", "id": kategori.id})


def ubah_kategori(id_kategori):
    db: Session = next(get_db())
    body = request.json
    kategori = db.query(Kategori).filter(Kategori.id == id_kategori).first()
    if not kategori:
        return jsonify({"kesalahan": "Kategori tidak ditemukan"}), 404

    for k, v in body.items():
        setattr(kategori, k, v)
    kategori.diperbarui_pada = datetime.utcnow()
    db.commit()
    return jsonify({"pesan": "Kategori berhasil diperbarui"})


def hapus_kategori(id_kategori):
    db: Session = next(get_db())
    kategori = db.query(Kategori).filter(Kategori.id == id_kategori).first()
    if not kategori:
        return jsonify({"kesalahan": "Kategori tidak ditemukan"}), 404

    db.delete(kategori)
    db.commit()
    return jsonify({"pesan": "Kategori berhasil dihapus"})
