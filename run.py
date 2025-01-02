from app import app
import os

if __name__ == "__main__":
    # run_with_ngrok(app)  # Ngrok ile çalıştır
    app.config['DEBUG'] = True  # Debug modunu burada ayarlayın
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
