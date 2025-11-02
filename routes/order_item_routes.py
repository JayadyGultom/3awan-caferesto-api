from flask import Blueprint
from controllers.order_item_controller import (
    get_semua_detail_pesanan,
    tambah_detail_pesanan,
    ubah_detail_pesanan,
    hapus_detail_pesanan,
)

detail_pesanan_routes = Blueprint("detail_pesanan_routes", __name__)

detail_pesanan_routes.route("/detail-pesanan", methods=["GET"])(get_semua_detail_pesanan)
detail_pesanan_routes.route("/detail-pesanan", methods=["POST"])(tambah_detail_pesanan)
detail_pesanan_routes.route("/detail-pesanan/<int:id_detail>", methods=["PUT"])(ubah_detail_pesanan)
detail_pesanan_routes.route("/detail-pesanan/<int:id_detail>", methods=["DELETE"])(hapus_detail_pesanan)
