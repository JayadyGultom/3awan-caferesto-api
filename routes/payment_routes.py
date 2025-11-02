from flask import Blueprint
from controllers.payment_controller import (
    get_semua_pembayaran,
    tambah_pembayaran,
    ubah_pembayaran,
    hapus_pembayaran,
)

pembayaran_routes = Blueprint("pembayaran_routes", __name__)

pembayaran_routes.route("/pembayaran", methods=["GET"])(get_semua_pembayaran)
pembayaran_routes.route("/pembayaran", methods=["POST"])(tambah_pembayaran)
pembayaran_routes.route("/pembayaran/<int:id_pembayaran>", methods=["PUT"])(ubah_pembayaran)
pembayaran_routes.route("/pembayaran/<int:id_pembayaran>", methods=["DELETE"])(hapus_pembayaran)
