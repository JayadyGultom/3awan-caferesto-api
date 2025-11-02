from flask import jsonify, request
from sqlalchemy.orm import Session
from datetime import datetime
from config.database import get_db
from models.order_model import Pesanan


def get_semua_pesanan():
    db: Session = next(get_db())
    data = db.query(Pesanan).all()
    return jsonify([
        {
            "id": p.id,
            "pelanggan_id": p.pelanggan_id,
            "status_pembayaran_id": p.status_pembayaran_id,
            "status_pengiriman_id": p.status_pengiriman_id,
            "total": float(p.total or 0),
            "tanggal_pesanan": p.tanggal_pesanan.strftime("%Y-%m-%d %H:%M:%S"),
        } for p in data
    ])


def tambah_pesanan():
    db: Session = next(get_db())
    body = request.json

    pesanan = Pesanan(
        pelanggan_id=body["pelanggan_id"],
        status_pembayaran_id=body["status_pembayaran_id"],
        status_pengiriman_id=body["status_pengiriman_id"],
        total=body.get("total", 0),
        tanggal_pesanan=datetime.strptime(body["tanggal_pesanan"], "%Y-%m-%d %H:%M:%S"),
    )
    db.add(pesanan)
    db.commit()
    db.refresh(pesanan)
    return jsonify({"pesan": "Pesanan berhasil ditambahkan", "id": pesanan.id})


def ubah_pesanan(id_pesanan):
    db: Session = next(get_db())
    body = request.json
    pesanan = db.query(Pesanan).filter(Pesanan.id == id_pesanan).first()
    if not pesanan:
        return jsonify({"kesalahan": "Pesanan tidak ditemukan"}), 404

    for k, v in body.items():
        setattr(pesanan, k, v)
    pesanan.diperbarui_pada = datetime.utcnow()
    db.commit()
    return jsonify({"pesan": "Pesanan berhasil diperbarui"})


def hapus_pesanan(id_pesanan):
    db: Session = next(get_db())
    pesanan = db.query(Pesanan).filter(Pesanan.id == id_pesanan).first()
    if not pesanan:
        return jsonify({"kesalahan": "Pesanan tidak ditemukan"}), 404

    db.delete(pesanan)
    db.commit()
    return jsonify({"pesan": "Pesanan berhasil dihapus"})
