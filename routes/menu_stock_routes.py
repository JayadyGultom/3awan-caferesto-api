from flask import Blueprint
from controllers.menu_stock_controller import (
    get_semua_stok_menu,
    tambah_stok_menu,
    ubah_stok_menu,
    hapus_stok_menu,
)

stok_routes = Blueprint("stok_routes", __name__)

stok_routes.route("/stok-menu", methods=["GET"])(get_semua_stok_menu)
stok_routes.route("/stok-menu", methods=["POST"])(tambah_stok_menu)
stok_routes.route("/stok-menu/<int:id_stok>", methods=["PUT"])(ubah_stok_menu)
stok_routes.route("/stok-menu/<int:id_stok>", methods=["DELETE"])(hapus_stok_menu)
