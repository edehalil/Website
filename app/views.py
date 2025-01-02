from flask import render_template, request, redirect, url_for, flash
from .models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

def ana_sayfa():
    return render_template('ana_sayfa.html')

def admin():
    return render_template('admin.html')

def urunlerimiz():
    return render_template('urunlerimiz.html')

def projelerimiz():
    return render_template('projelerimiz.html')

def en_yakin_magaza():
    return render_template('en_yakin_magaza.html')

def hakkimizda():
    return render_template('hakkimizda.html')

def iletisim():
    return render_template('iletisim.html')

def sikca_sorulan_sorular():
    return render_template('sikca_sorulan_sorular.html')

def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            return redirect(url_for('admin_dashboard'))
    return render_template('admin.html')

def admin_register():
    if request.method == 'POST':
        key = request.form.get('key')
        if not key:
            flash('Key is required', 'error')
            return redirect(url_for('admin_register'))
        if key != "BenAslindaYokum":
            flash('Invalid Key', 'error')
            return redirect(url_for('admin_register'))
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        phone = request.form['phone']
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        if password == confirm_password:
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
            new_user = User(first_name=first_name, last_name=last_name, phone=phone, username=username, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('admin'))
    return render_template('admin_register.html')

def admin_forget():
    if request.method == 'POST':
        phone = request.form['phone']
        user = User.query.filter_by(phone=phone).first()
        if user:
            return redirect(url_for('admin_reset_password', user_id=user.id))
    return render_template('forget.html')

def admin_reset_password(user_id):
    user = User.query.get(user_id)
    if request.method == 'POST':
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        if password == confirm_password:
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
            user.password = hashed_password
            db.session.commit()
            return redirect(url_for('admin'))
    return render_template('reset_password.html', user=user)

def admin_dashboard():
    users = User.query.all()
    return render_template('admin_dashboard.html', users=users)

def admin_delete(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
    return redirect(url_for('admin_dashboard'))
