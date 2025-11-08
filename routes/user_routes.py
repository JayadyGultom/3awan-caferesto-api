from flask import Blueprint, request, jsonify
from flask_cors import cross_origin  # ✅ biar Flutter Web bisa akses
from sqlalchemy.orm import Session
from config.database import get_db
from models.user_account_model import Pengguna
from werkzeug.security import generate_password_hash, check_password_hash

pengguna_routes = Blueprint("pengguna_routes", __name__)


# 🟢 REGISTER PENGGUNA
@pengguna_routes.route("/pengguna/register", methods=["POST"])
@cross_origin()  # izinkan akses Flutter Web
def register_pengguna():
    db: Session = next(get_db())
    try:
        data = request.get_json(force=True, silent=True)
        email = data.get("email")
        sandi = data.get("sandi_hash")
        peran = data.get("peran", "pelanggan")
        status = data.get("status", "aktif")

        # Validasi input
        if not email or not sandi:
            return jsonify({
                "success": False,
                "message": "Email dan sandi wajib diisi"
            }), 400

        # Cek apakah email sudah terdaftar
        existing = db.query(Pengguna).filter_by(email=email).first()
        if existing:
            return jsonify({
                "success": False,
                "message": "Email sudah digunakan"
            }), 409

        # Hash password sebelum disimpan
        sandi_hash = generate_password_hash(sandi)

        pengguna_baru = Pengguna(
            email=email,
            sandi_hash=sandi_hash,
            peran=peran,
            status=status
        )

        db.add(pengguna_baru)
        db.commit()
        db.refresh(pengguna_baru)

        return jsonify({
            "success": True,
            "message": "Registrasi berhasil",
            "data": {
                "id": pengguna_baru.id,
                "email": pengguna_baru.email,
                "peran": pengguna_baru.peran,
                "status": pengguna_baru.status
            }
        }), 201

    except Exception as e:
        db.rollback()
        print("Error register:", e)
        return jsonify({
            "success": False,
            "message": f"Terjadi kesalahan server: {e}"
        }), 500

    finally:
        db.close()


# 🟠 LOGIN PENGGUNA
@pengguna_routes.route("/pengguna/login", methods=["POST"])
@cross_origin()  # izinkan akses Flutter Web
def login_pengguna():
    db: Session = next(get_db())
    try:
        data = request.get_json(force=True, silent=True)
        email = data.get("email")
        sandi = data.get("sandi_hash")

        # Validasi input
        if not email or not sandi:
            return jsonify({
                "success": False,
                "message": "Email dan kata sandi wajib diisi"
            }), 400

        pengguna = db.query(Pengguna).filter_by(email=email).first()

        if not pengguna:
            return jsonify({
                "success": False,
                "message": "Email tidak ditemukan"
            }), 404

        # Cek apakah password cocok
        if not check_password_hash(pengguna.sandi_hash, sandi):
            return jsonify({
                "success": False,
                "message": "Kata sandi salah"
            }), 401

        # Jika cocok
        return jsonify({
            "success": True,
            "message": "Login berhasil",
            "data": {
                "id": pengguna.id,
                "email": pengguna.email,
                "peran": pengguna.peran,
                "status": pengguna.status
            }
        }), 200

    except Exception as e:
        print("Error login:", e)
        return jsonify({
            "success": False,
            "message": f"Terjadi kesalahan server: {e}"
        }), 500

    finally:
        db.close()
