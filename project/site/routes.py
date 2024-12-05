from flask import Blueprint, render_template



site = Blueprint('site', __name__, template_folder="templates")


@site.route('/')
def home():
	return render_template("home.html")



@site.route('/about')
def about():
	return render_template("about.html")




@site.route('/contact')
def contact():
	return render_template("contact.html")