from flask import Flask
from flask_cors import CORS  # 🔥 tambahkan ini
from config.database import engine, Base
import models
from routes import semua_routes
import os

app = Flask(__name__)

# ✅ Izinkan semua domain mengakses API (saat pengembangan)
CORS(app, resources={r"/*": {"origins": "*"}})

# Buat tabel otomatis
Base.metadata.create_all(bind=engine)

# ✅ Seed data awal (jika belum ada)
try:
    from seed_data import seed_status_pembayaran, seed_status_pengiriman, seed_kategori
    print("🌱 Checking initial data...")
    seed_status_pembayaran()
    seed_status_pengiriman()
    seed_kategori()
    print("✅ Initial data check completed!")
except Exception as e:
    print(f"⚠️ Warning: Could not seed initial data: {e}")
    print("💡 You can run 'python seed_data.py' manually if needed")

# Daftarkan semua routes
for r in semua_routes:
    app.register_blueprint(r)

@app.route("/")
def home():
    return {"message": "API is running"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)
