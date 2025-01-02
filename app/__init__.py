from flask import Flask
from .views import ana_sayfa, admin, urunlerimiz, projelerimiz, en_yakin_magaza, hakkimizda, admin_login, admin_register, admin_forget, admin_dashboard, admin_delete, admin_reset_password
from .models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'BenAslindaYokum'

db.init_app(app)

with app.app_context():
    db.create_all()

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
    app.run(debug=True)
