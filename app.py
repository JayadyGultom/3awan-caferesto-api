from flask import Flask
from config.database import engine, Base
import models  # register semua model
from routes import semua_routes
import os

app = Flask(__name__)

# Buat tabel otomatis
Base.metadata.create_all(bind=engine)

# Daftarkan semua routes
for r in semua_routes:
    app.register_blueprint(r)

# Tambah route root sederhana (biar Railway tahu aplikasi hidup)
@app.route("/")
def home():
    return {"message": "API is running"}

# 🧠 Tambahkan ini untuk debugging
if __name__ == "__main__":
    print("=== Routes Terdaftar ===")
    for rule in app.url_map.iter_rules():
        print(rule)
    print("========================")

    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)
