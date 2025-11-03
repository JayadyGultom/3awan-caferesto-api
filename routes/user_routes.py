from flask import Blueprint, request, jsonify
from config.database import SessionLocal
from models.user_account_model import Pengguna

pengguna_routes = Blueprint("pengguna_routes", __name__)
session = SessionLocal()

@pengguna_routes.route("/pengguna/login", methods=["POST"])
def login_pengguna():
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

        # Cek apakah email dan password cocok
        pengguna = (
            session.query(Pengguna)
            .filter_by(email=email, sandi_hash=sandi)
            .first()
        )

        if not pengguna:
            return jsonify({
                "success": False,
                "message": "Email atau kata sandi salah"
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
        session.close()
