from flask import Blueprint
from controllers.customer_address_controller import (
    get_semua_alamat,
    tambah_alamat,
    ubah_alamat,
    hapus_alamat,
)

alamat_routes = Blueprint("alamat_routes", __name__)

alamat_routes.route("/alamat", methods=["GET"])(get_semua_alamat)
alamat_routes.route("/alamat", methods=["POST"])(tambah_alamat)
alamat_routes.route("/alamat/<int:id_alamat>", methods=["PUT"])(ubah_alamat)
alamat_routes.route("/alamat/<int:id_alamat>", methods=["DELETE"])(hapus_alamat)
