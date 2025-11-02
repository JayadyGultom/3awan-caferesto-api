from flask import Blueprint
from controllers.category_controller import (
    get_semua_kategori,
    tambah_kategori,
    ubah_kategori,
    hapus_kategori,
)

kategori_routes = Blueprint("kategori_routes", __name__)

kategori_routes.route("/kategori", methods=["GET"])(get_semua_kategori)
kategori_routes.route("/kategori", methods=["POST"])(tambah_kategori)
kategori_routes.route("/kategori/<int:id_kategori>", methods=["PUT"])(ubah_kategori)
kategori_routes.route("/kategori/<int:id_kategori>", methods=["DELETE"])(hapus_kategori)
