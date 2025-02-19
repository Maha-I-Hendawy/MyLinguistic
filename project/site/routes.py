from flask import Blueprint, render_template, request, flash, url_for
#from project import mail
#from flask_mail import Message 
#from form import MessageForm



site = Blueprint('site', __name__, template_folder="templates")




@site.route('/')
@site.route('/home')
def home():
	return render_template('site/home.html')



@site.route('/about')
def about():
	return render_template('site/about.html', title='About Us Page')



@site.route('/products')
def products():
	return render_template('site/products.html', title='Products')


@site.route('/services')
def services():
	return render_template('site/services.html', title='Services')



@site.route('/contact', methods=['GET', 'POST'])
def contact():
	"""
	form = MessageForm()
	if form.validate_on_submit():
		msg = Message(form.title.data, recipients=['lydialankcaster@gmail.com']) # Provide email address you want to send emails to from your default email provided above
		msg.body = f'''From: {form.name.data}, {form.email.data},
		Message: {form.message.data}'''
		mail.send(msg)
		flash('Your message has been sent.', 'success')
		return redirect(url_for('home'))
	"""
	return render_template('site/contact.html', title='Contact Us')
