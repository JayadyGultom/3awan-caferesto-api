from flask import Blueprint
from controllers.order_controller import (
    get_semua_pesanan,
    tambah_pesanan,
    ubah_pesanan,
    hapus_pesanan,
)

pesanan_routes = Blueprint("pesanan_routes", __name__)

pesanan_routes.route("/pesanan", methods=["GET"])(get_semua_pesanan)
pesanan_routes.route("/pesanan", methods=["POST"])(tambah_pesanan)
pesanan_routes.route("/pesanan/<int:id_pesanan>", methods=["PUT"])(ubah_pesanan)
pesanan_routes.route("/pesanan/<int:id_pesanan>", methods=["DELETE"])(hapus_pesanan)
