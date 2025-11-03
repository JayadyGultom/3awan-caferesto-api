from flask import Flask
from flask_cors import CORS  # ✅ Tambahkan import ini
from config.database import engine, Base
import models  # register semua model
from routes import semua_routes
import os

app = Flask(__name__)

# ✅ Aktifkan CORS untuk semua route dan semua origin
CORS(app)

# Buat tabel otomatis (jika belum ada)
Base.metadata.create_all(bind=engine)

# Daftarkan semua blueprint dari routes/
for r in semua_routes:
    app.register_blueprint(r)

# Route root sederhana, untuk uji koneksi API dari Railway
@app.route("/")
def home():
    return {"message": "API is running and CORS is enabled ✅"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # gunakan port Railway
    app.run(debug=False, host="0.0.0.0", port=port)
