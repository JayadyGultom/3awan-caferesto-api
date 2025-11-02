from routes.user_routes import pengguna_routes
from routes.customer_routes import pelanggan_routes
from routes.customer_address_routes import alamat_routes
from routes.category_routes import kategori_routes
from routes.menu_routes import menu_routes
from routes.menu_stock_routes import stok_routes
from routes.order_routes import pesanan_routes
from routes.order_item_routes import detail_pesanan_routes
from routes.payment_routes import pembayaran_routes
from routes.payment_status_routes import status_pembayaran_routes
from routes.delivery_status_routes import status_pengiriman_routes

semua_routes = [
    pengguna_routes,
    pelanggan_routes,
    alamat_routes,
    kategori_routes,
    menu_routes,
    stok_routes,
    pesanan_routes,
    detail_pesanan_routes,
    pembayaran_routes,
    status_pembayaran_routes,
    status_pengiriman_routes,
]
