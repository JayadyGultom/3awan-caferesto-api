from flask import jsonify, request
from sqlalchemy.orm import Session
from datetime import datetime
from config.database import get_db
from models.customer_model import Pelanggan


def get_semua_pelanggan():
    db: Session = next(get_db())
    data = db.query(Pelanggan).all()
    return jsonify([
        {
            "id": p.id,
            "pengguna_id": p.pengguna_id,
            "nama_lengkap": p.nama_lengkap,
            "telepon": p.telepon,
        } for p in data
    ])


def tambah_pelanggan():
    db: Session = next(get_db())
    body = request.json

    pelanggan = Pelanggan(
        pengguna_id=body["pengguna_id"],
        nama_lengkap=body["nama_lengkap"],
        telepon=body.get("telepon"),
    )
    db.add(pelanggan)
    db.commit()
    db.refresh(pelanggan)
    return jsonify({"pesan": "Pelanggan berhasil ditambahkan", "id": pelanggan.id})


def ubah_pelanggan(id_pelanggan):
    db: Session = next(get_db())
    body = request.json
    pelanggan = db.query(Pelanggan).filter(Pelanggan.id == id_pelanggan).first()
    if not pelanggan:
        return jsonify({"kesalahan": "Pelanggan tidak ditemukan"}), 404

    for k, v in body.items():
        setattr(pelanggan, k, v)
    pelanggan.diperbarui_pada = datetime.utcnow()
    db.commit()
    return jsonify({"pesan": "Pelanggan berhasil diperbarui"})


def hapus_pelanggan(id_pelanggan):
    db: Session = next(get_db())
    pelanggan = db.query(Pelanggan).filter(Pelanggan.id == id_pelanggan).first()
    if not pelanggan:
        return jsonify({"kesalahan": "Pelanggan tidak ditemukan"}), 404

    db.delete(pelanggan)
    db.commit()
    return jsonify({"pesan": "Pelanggan berhasil dihapus"})
