from app import app
from flask_ngrok import run_with_ngrok

if __name__ == "__main__":
    run_with_ngrok(app)  # Ngrok ile çalıştır
    app.config['DEBUG'] = True  # Debug modunu burada ayarlayın
    app.run()
