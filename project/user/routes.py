from project import app, db
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from project.models import User


user = Blueprint('user', __name__, template_folder="templates")






@user.route('/register', methods=['GET', 'POST'])
def register():
	users = User.query.all()
	if request.method == 'POST':
		username = request.form["username"]
		email = request.form["email"]
		password = request.form["password"]
		confirm_password = request.form["confirm_password"]
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
			return redirect(url_for('user.login'))
			
	return render_template("user/register.html", title="Registration Page")




@user.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		username = request.form.get("username")
		password = request.form.get("password")

		user = User.query.filter_by(username=username).first()

		if user and check_password_hash(user.password, password):
			session["user"] = user.username
			flash(f"Welcome {user.username}")
			return redirect(url_for('user.profile'))

	return render_template("user/login.html", title="Login Page")



@user.route('/logout')
def logout():
	if 'user' in session:
		session.pop('user', None)
		return redirect(url_for('user.login'))
	else:
		return redirect(url_for('user.login'))




@user.route('/profile')
def profile():
	if 'user' in session:
		user_id = session['user']
		userr = User.query.filter_by(user_id=user_id).first()
		return render_template("user/profile.html", userr=userr)
	else:
		return redirect(url_for('user.login'))




"""

@app.route('/profile')
def profile():
	if 'user' in session:
		user = session['user']
		user.form["username"] = user.username 
		user.form["email"] = user.email 
	return render_template("profile.html")

"""

# check first if user is in session and user permissions or roles

@app.route('/user', methods=["GET", "POST"])
def adduser():
	if request.method == 'POST':
		username = request.form.get("username")
		email = request.form.get("email")
		password = request.form.get("password")
		hashed_password = generate_password_hash(password)
		user = User(username=username, email=email, password=password)
		db.session.add(user)
		db.session.commit()
		return redirect(url_for('getusers'))
	return render_template("adduser.html")



@app.route('/getusers')
def getusers():
	users = User.query.all()

	return render_template("getallusers.html", users=users)



@app.route('/getuser/<int:id>')
def getuser(id):
	user = User.query.filter_by(id=id).first()
	return render_template("userinfo.html", user=user)



@app.route('/updateuser/<int:id>', methods=["GET", "POST"])
def updateuser(id):
	if request.method == 'POST':
		user = User.query.filter_by(id=id).first()
		user.username = request.form.get("username")
		user.email = request.form.get("email")
		user.password = request.form.get("password")
		db.session.commit()
		return redirect(url_for("getuser", id=id))

	

	return render_template("updateuser.html")


@app.route("/deleteuser/<int:id>")
def deleteuser(id):
	user = User.query.filter_by(id=id).delete()
	db.session.commit()
	return redirect(url_for("getusers"))

