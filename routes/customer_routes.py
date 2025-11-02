from flask import Blueprint
from controllers.customer_controller import (
    get_semua_pelanggan,
    tambah_pelanggan,
    ubah_pelanggan,
    hapus_pelanggan,
)

pelanggan_routes = Blueprint("pelanggan_routes", __name__)

pelanggan_routes.route("/pelanggan", methods=["GET"])(get_semua_pelanggan)
pelanggan_routes.route("/pelanggan", methods=["POST"])(tambah_pelanggan)
pelanggan_routes.route("/pelanggan/<int:id_pelanggan>", methods=["PUT"])(ubah_pelanggan)
pelanggan_routes.route("/pelanggan/<int:id_pelanggan>", methods=["DELETE"])(hapus_pelanggan)
