from project import app, db
from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from .models import User


user = Blueprint('user', __name__, template_folder="templates")






@user.route('/register', methods=['GET', 'POST'])
def register():
	users = User.query.all()
	if request.method == 'POST':
		username = request.form.get("username")
		email = request.form.get("email")
		password = request.form.get("password")
		confirm_password = request.form.get("confirm_password")
		for user in users:
			if user.username == username:
				flash("Username already exists")
			if user.email == email:
				flash("Email already exists")

		if password == confirm_password:
			hashed_password = generate_password_hash(password)
			user = User(username=username, email=email, password=hashed_password)
			db.session.add(user)
			db.session.commit()
			return redirect(url_for('login'))
			
	return render_template("user/register.html", title="Registration Page")




@user.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		username = request.form.get("username")
		password = request.form.get("password")

		user = User.query.filter_by(username=username).first()

		if user and check_password_hash(user.password, password):
			session["user"] = user.user_id
			flash(f"Welcome {user.username}")
			return redirect(url_for('profile'))

	return render_template("user/login.html", title="Login Page")



@user.route('/logout')
def logout():
	if 'user' in session:
		session.pop('user', None)
		return redirect(url_for('login'))
	else:
		return redirect(url_for('login'))




@user.route('/profile')
def profile():
	if 'user' in session:
		user_id = session['user']
		user = User.query.filter_by(user_id=user_id).first()
		return render_template("profile.html", user=user)
	else:
		return redirect(url_for('login'))
