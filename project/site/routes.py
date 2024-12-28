from flask import Blueprint, render_template, request, flash, url_for



site = Blueprint('site', __name__, template_folder="templates")


@site.route('/')
def home():
	return render_template("site/home.html")



@site.route('/about')
def about():
	return render_template("site/about.html")




@site.route('/contact')
def contact():
	if request.method == 'POST':
		first_name = request.form['firstname']
		last_name = request.form['lastname']
		email = request.form['email']
		message = request.form['message']
	return render_template("site/contact.html")