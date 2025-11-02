from flask import Blueprint
from controllers.user_account_controller import (
    get_semua_pengguna,
    tambah_pengguna,
    ubah_pengguna,
    hapus_pengguna,
)

pengguna_routes = Blueprint("pengguna_routes", __name__)

pengguna_routes.route("/pengguna", methods=["GET"])(get_semua_pengguna)
pengguna_routes.route("/pengguna", methods=["POST"])(tambah_pengguna)
pengguna_routes.route("/pengguna/<int:id_pengguna>", methods=["PUT"])(ubah_pengguna)
pengguna_routes.route("/pengguna/<int:id_pengguna>", methods=["DELETE"])(hapus_pengguna)
