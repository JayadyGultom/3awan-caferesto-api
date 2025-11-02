from flask import Blueprint
from controllers.menu_controller import (
    get_semua_menu,
    tambah_menu,
    ubah_menu,
    hapus_menu,
)

menu_routes = Blueprint("menu_routes", __name__)

menu_routes.route("/menu", methods=["GET"])(get_semua_menu)
menu_routes.route("/menu", methods=["POST"])(tambah_menu)
menu_routes.route("/menu/<int:id_menu>", methods=["PUT"])(ubah_menu)
menu_routes.route("/menu/<int:id_menu>", methods=["DELETE"])(hapus_menu)
