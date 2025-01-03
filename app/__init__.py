from flask import Flask, redirect
import os
from .views import ana_sayfa, admin, urunlerimiz, projelerimiz, en_yakin_magaza, hakkimizda, admin_login, admin_register, admin_forget, admin_dashboard, admin_delete, admin_reset_password
from .models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'BenAslindaYokum'

db.init_app(app)

with app.app_context():
    db.create_all()

# Dinamik URL'yi saklamak için bir değişken kullanıyoruz
current_dynamic_url = "https://guys.com/initial-dynamic-link"

# Dinamik URL'yi sabit bir link üzerinden yönlendiren route
@app.route('/sabit')
def sabit_link():
    global current_dynamic_url
    return redirect(current_dynamic_url, code=302)

# Dinamik URL'yi güncellemek için bir admin endpoint (isteğe bağlı)
@app.route('/update_url/<path:new_url>')
def update_url(new_url):
    global current_dynamic_url
    current_dynamic_url = f"https://{new_url}"  # Yeni URL'yi ayarla
    return f"URL başarıyla güncellendi: {current_dynamic_url}"

app.add_url_rule('/', 'ana_sayfa', ana_sayfa)
app.add_url_rule('/admin', 'admin', admin, methods=['GET', 'POST'])
app.add_url_rule('/admin/login', 'admin_login', admin_login, methods=['GET', 'POST'])
app.add_url_rule('/admin/register', 'admin_register', admin_register, methods=['GET', 'POST'])
app.add_url_rule('/admin/forget', 'admin_forget', admin_forget, methods=['GET', 'POST'])
app.add_url_rule('/admin/reset_password/<int:user_id>', 'admin_reset_password', admin_reset_password, methods=['GET', 'POST'])
app.add_url_rule('/admin/dashboard', 'admin_dashboard', admin_dashboard)
app.add_url_rule('/admin/delete/<int:user_id>', 'admin_delete', admin_delete, methods=['POST'])
app.add_url_rule('/urunlerimiz', 'urunlerimiz', urunlerimiz)
app.add_url_rule('/projelerimiz', 'projelerimiz', projelerimiz)
app.add_url_rule('/en_yakin_magaza', 'en_yakin_magaza', en_yakin_magaza)
app.add_url_rule('/hakkimizda', 'hakkimizda', hakkimizda)

if __name__ == "__main__":
    app.config['DEBUG'] = True  # Debug modunu burada ayarlayın
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
