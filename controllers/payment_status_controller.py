from flask import jsonify, request
from sqlalchemy.orm import Session
from config.database import get_db
from models.payment_status_model import StatusPembayaran


def get_semua_status_pembayaran():
    db: Session = next(get_db())
    data = db.query(StatusPembayaran).all()
    return jsonify([{"id": s.id, "nama_status": s.nama_status} for s in data])


def tambah_status_pembayaran():
    db: Session = next(get_db())
    body = request.json
    status = StatusPembayaran(nama_status=body["nama_status"])
    db.add(status)
    db.commit()
    db.refresh(status)
    return jsonify({"pesan": "Status pembayaran berhasil ditambahkan", "id": status.id})


def hapus_status_pembayaran(id_status):
    db: Session = next(get_db())
    status = db.query(StatusPembayaran).filter(StatusPembayaran.id == id_status).first()
    if not status:
        return jsonify({"kesalahan": "Status tidak ditemukan"}), 404

    db.delete(status)
    db.commit()
    return jsonify({"pesan": "Status pembayaran berhasil dihapus"})
