from flask import Blueprint
from controllers.payment_status_controller import (
    get_semua_status_pembayaran,
    tambah_status_pembayaran,
    hapus_status_pembayaran,
)

status_pembayaran_routes = Blueprint("status_pembayaran_routes", __name__)

status_pembayaran_routes.route("/status-pembayaran", methods=["GET"])(get_semua_status_pembayaran)
status_pembayaran_routes.route("/status-pembayaran", methods=["POST"])(tambah_status_pembayaran)
status_pembayaran_routes.route("/status-pembayaran/<int:id_status>", methods=["DELETE"])(hapus_status_pembayaran)
