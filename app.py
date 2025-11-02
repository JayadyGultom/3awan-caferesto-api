from flask import Flask
from config.database import engine, Base
import models  # register semua model
from routes import semua_routes

app = Flask(__name__)

# Buat tabel otomatis
Base.metadata.create_all(bind=engine)

# Daftarkan semua routes
for r in semua_routes:
    app.register_blueprint(r)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8080))
    app.run(debug=False, host="0.0.0.0", port=port)
