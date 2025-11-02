from flask import jsonify, request
from sqlalchemy.orm import Session
from datetime import datetime
from config.database import get_db
from models.order_item_model import DetailPesanan


def get_semua_detail_pesanan():
    db: Session = next(get_db())
    data = db.query(DetailPesanan).all()
    return jsonify([
        {
            "id": d.id,
            "pesanan_id": d.pesanan_id,
            "menu_id": d.menu_id,
            "jumlah": d.jumlah,
            "harga_saat_pesanan": float(d.harga_saat_pesanan),
        } for d in data
    ])


def tambah_detail_pesanan():
    db: Session = next(get_db())
    body = request.json

    detail = DetailPesanan(
        pesanan_id=body["pesanan_id"],
        menu_id=body["menu_id"],
        jumlah=body["jumlah"],
        harga_saat_pesanan=body["harga_saat_pesanan"]
    )
    db.add(detail)
    db.commit()
    db.refresh(detail)
    return jsonify({"pesan": "Detail pesanan berhasil ditambahkan", "id": detail.id})


def ubah_detail_pesanan(id_detail):
    db: Session = next(get_db())
    body = request.json
    detail = db.query(DetailPesanan).filter(DetailPesanan.id == id_detail).first()
    if not detail:
        return jsonify({"kesalahan": "Detail pesanan tidak ditemukan"}), 404

    for k, v in body.items():
        setattr(detail, k, v)
    detail.diperbarui_pada = datetime.utcnow()
    db.commit()
    return jsonify({"pesan": "Detail pesanan berhasil diperbarui"})


def hapus_detail_pesanan(id_detail):
    db: Session = next(get_db())
    detail = db.query(DetailPesanan).filter(DetailPesanan.id == id_detail).first()
    if not detail:
        return jsonify({"kesalahan": "Detail pesanan tidak ditemukan"}), 404

    db.delete(detail)
    db.commit()
    return jsonify({"pesan": "Detail pesanan berhasil dihapus"})
