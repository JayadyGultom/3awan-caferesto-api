from flask import Blueprint
from controllers.delivery_status_controller import (
    get_semua_status_pengiriman,
    tambah_status_pengiriman,
    hapus_status_pengiriman,
)

status_pengiriman_routes = Blueprint("status_pengiriman_routes", __name__)

status_pengiriman_routes.route("/status-pengiriman", methods=["GET"])(get_semua_status_pengiriman)
status_pengiriman_routes.route("/status-pengiriman", methods=["POST"])(tambah_status_pengiriman)
status_pengiriman_routes.route("/status-pengiriman/<int:id_status>", methods=["DELETE"])(hapus_status_pengiriman)
