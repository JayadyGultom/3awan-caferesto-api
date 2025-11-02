from flask import jsonify, request
from sqlalchemy.orm import Session
from datetime import datetime
from config.database import get_db
from models.user_account_model import Pengguna


def get_semua_pengguna():
    db: Session = next(get_db())
    data = db.query(Pengguna).all()
    return jsonify([
        {
            "id": p.id,
            "email": p.email,
            "peran": p.peran,
            "status": p.status,
            "dibuat_pada": p.dibuat_pada,
            "diperbarui_pada": p.diperbarui_pada
        } for p in data
    ])


def tambah_pengguna():
    db: Session = next(get_db())
    body = request.json

    pengguna = Pengguna(
        email=body["email"],
        sandi_hash=body["sandi_hash"],
        peran=body.get("peran", "pelanggan"),
        status=body.get("status", "aktif"),
    )

    db.add(pengguna)
    db.commit()
    db.refresh(pengguna)
    return jsonify({"pesan": "Pengguna berhasil ditambahkan", "id": pengguna.id})


def ubah_pengguna(id_pengguna):
    db: Session = next(get_db())
    body = request.json
    pengguna = db.query(Pengguna).filter(Pengguna.id == id_pengguna).first()
    if not pengguna:
        return jsonify({"kesalahan": "Pengguna tidak ditemukan"}), 404

    for k, v in body.items():
        setattr(pengguna, k, v)
    pengguna.diperbarui_pada = datetime.utcnow()
    db.commit()
    return jsonify({"pesan": "Pengguna berhasil diperbarui"})


def hapus_pengguna(id_pengguna):
    db: Session = next(get_db())
    pengguna = db.query(Pengguna).filter(Pengguna.id == id_pengguna).first()
    if not pengguna:
        return jsonify({"kesalahan": "Pengguna tidak ditemukan"}), 404

    db.delete(pengguna)
    db.commit()
    return jsonify({"pesan": "Pengguna berhasil dihapus"})
