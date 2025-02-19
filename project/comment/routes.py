from project import db
from flask import Blueprint, render_template, url_for, redirect, session
#from .forms import TodoForm, UpdateTodoForm
from project.user.routes import * 
from project.post.routes import *
from project.models import Comment



comment = Blueprint('comment', __name__, template_folder='templates')



@comment.route('/', methods=['GET', 'POST'])
def index():
	if 'user' in session:
		user_id = session['user_id']
		if request.method == 'POST':
			comment = request.form['comment']
			new_comment = Commenr(comment=comment)
			db.session.add(new_comment)
			db.session.commit()
			return redirect(request.url)
		elif request.method == 'GET':
			comments = Comment.query.all()
		return render_template('post/get_post.html', comments=comments)
		
	else:
		return redirect(url_for('user.login'))



@comment.route('/comment/<int:comment_id>')
def one_comment(comment_id):
	if 'user' in session:

		comment = Comment.query.get_or_404(comment_id)

		return render_template('comment.html', comment=comment)
	else:
		return redirect(url_for('user.login'))


@comment.route('/comment/<int:comment_id>/update', methods=['GET', 'POST'])
def update_comment(comment_id):
	if 'user' in session:
		comment = Comment.query.get_or_404(comment_id)
		if request.method == 'POST':
			comment.comment = request.form['comment']
			db.session.commit()
			return redirect(url_for('index'))


		return render_template('update_comment.html', comment=comment)

	else:
		return redirect(url_for('user.login'))


@comment.route('/comment/<int:comment_id>/delete', methods=['GET', 'POST'])
def delete_comment(comment_id):
	if 'user' in session:

		comment = Comment.query.get_or_404(comment_id)
		db.session.delete(comment)
		db.session.commit()
		return redirect(url_for('index'))

	else:
		return redirect(url_for('user.login'))
