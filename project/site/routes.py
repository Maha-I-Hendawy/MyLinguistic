from flask import Blueprint, render_template



site = Blueprint('site', __name__, template_folder="templates")


@site.route('/')
def home():
	return render_template("site/home.html")



@site.route('/about')
def about():
	return render_template("site/about.html")




@site.route('/contact')
def contact():
	return render_template("site/contact.html")