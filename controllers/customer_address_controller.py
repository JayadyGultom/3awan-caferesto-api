from flask import jsonify, request
from sqlalchemy.orm import Session
from datetime import datetime
from config.database import get_db
from models.customer_address_model import AlamatPelanggan


def get_semua_alamat():
    db: Session = next(get_db())
    data = db.query(AlamatPelanggan).all()
    return jsonify([
        {
            "id": a.id,
            "pelanggan_id": a.pelanggan_id,
            "alamat": a.alamat,
            "utama": a.utama,
        } for a in data
    ])


def tambah_alamat():
    db: Session = next(get_db())
    body = request.json

    alamat = AlamatPelanggan(
        pelanggan_id=body["pelanggan_id"],
        alamat=body.get("alamat"),
        utama=body.get("utama", False),
    )
    db.add(alamat)
    db.commit()
    db.refresh(alamat)
    return jsonify({"pesan": "Alamat pelanggan berhasil ditambahkan", "id": alamat.id})


def ubah_alamat(id_alamat):
    db: Session = next(get_db())
    body = request.json
    alamat = db.query(AlamatPelanggan).filter(AlamatPelanggan.id == id_alamat).first()
    if not alamat:
        return jsonify({"kesalahan": "Alamat tidak ditemukan"}), 404

    for k, v in body.items():
        setattr(alamat, k, v)
    alamat.diperbarui_pada = datetime.utcnow()
    db.commit()
    return jsonify({"pesan": "Alamat pelanggan berhasil diperbarui"})


def hapus_alamat(id_alamat):
    db: Session = next(get_db())
    alamat = db.query(AlamatPelanggan).filter(AlamatPelanggan.id == id_alamat).first()
    if not alamat:
        return jsonify({"kesalahan": "Alamat tidak ditemukan"}), 404

    db.delete(alamat)
    db.commit()
    return jsonify({"pesan": "Alamat pelanggan berhasil dihapus"})
