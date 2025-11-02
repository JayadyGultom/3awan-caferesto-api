from flask import jsonify, request
from sqlalchemy.orm import Session
from datetime import datetime
from config.database import get_db
from models.payment_model import Pembayaran


def get_semua_pembayaran():
    db: Session = next(get_db())
    data = db.query(Pembayaran).all()
    return jsonify([
        {
            "id": p.id,
            "pesanan_id": p.pesanan_id,
            "metode": p.metode,
            "jumlah": float(p.jumlah or 0),
            "tanggal_bayar": p.tanggal_bayar.strftime("%Y-%m-%d %H:%M:%S") if p.tanggal_bayar else None,
        } for p in data
    ])


def tambah_pembayaran():
    db: Session = next(get_db())
    body = request.json

    pembayaran = Pembayaran(
        pesanan_id=body["pesanan_id"],
        metode=body["metode"],
        jumlah=body.get("jumlah", 0),
        tanggal_bayar=datetime.strptime(body["tanggal_bayar"], "%Y-%m-%d %H:%M:%S")
        if body.get("tanggal_bayar") else None,
    )
    db.add(pembayaran)
    db.commit()
    db.refresh(pembayaran)
    return jsonify({"pesan": "Pembayaran berhasil ditambahkan", "id": pembayaran.id})


def ubah_pembayaran(id_pembayaran):
    db: Session = next(get_db())
    body = request.json
    pembayaran = db.query(Pembayaran).filter(Pembayaran.id == id_pembayaran).first()
    if not pembayaran:
        return jsonify({"kesalahan": "Pembayaran tidak ditemukan"}), 404

    for k, v in body.items():
        setattr(pembayaran, k, v)
    pembayaran.diperbarui_pada = datetime.utcnow()
    db.commit()
    return jsonify({"pesan": "Pembayaran berhasil diperbarui"})


def hapus_pembayaran(id_pembayaran):
    db: Session = next(get_db())
    pembayaran = db.query(Pembayaran).filter(Pembayaran.id == id_pembayaran).first()
    if not pembayaran:
        return jsonify({"kesalahan": "Pembayaran tidak ditemukan"}), 404

    db.delete(pembayaran)
    db.commit()
    return jsonify({"pesan": "Pembayaran berhasil dihapus"})
