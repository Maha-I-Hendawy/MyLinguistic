from project import db
from flask import Blueprint, request, jsonify
from project.models import User, Post, Comment
#user_schema, users_schema, post_schema, posts_schema, comment_schema, comments_schema, sentence_schema, sentences_schema
from werkzeug.security import generate_password_hash


api = Blueprint('api', __name__)


# Get Users

@api.route('/users', methods=['GET'])
def get_users():
	users = User.query.all()
	return jsonify({'users': users})

# Get One User

@api.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
	user = User.query.filter_by(user_id=user_id).first()
	return jsonify({'user', user})


# Add User

@api.route('/users', methods=['POST'])
def add_user():
	if request.method == 'POST':
		data = request.get_json()
		#hashed_password = generate_password_hash(data['password'])
		#user = User(username=data['username'], email=data['email'], password=hashed_password)
		#db.session.add(user)
		#db.session.commit()
		return jsonify(data)

	else:
		'add something'


# Update User

@api.route('/users/<int:user_id>/update', methods=['PUT'])
def update_user_profile(user_id):
	if request.method == 'PUT':
		user = User.query.filter_by(user_id=user_id).first()
		data = request.get_json()
		user.username = data['username']
		user.email = data['email']
		db.session.commit()
		return jsonify({'user': user})
	else:
		return 'Update user'


@api.route('/users/<int:user_id>/reset_password', methods=['PATCH'])
def reset_password(user_id):
	if request.method == 'PATCH':
		user = User.query.filter_by(user_id=user_id).first()
		data = request.get_json()
		new_hashed_password = generate_password_hash(data['password'])
		user.password = new_hashed_password
		return jsonify({'password': new_hashed_password})
	else:
		'change password'

# Delete User

@api.route('/users/<int:user_id>/delete', methods=['DELETE'])
def delete_user_account(user_id):
	if request.method == 'DELETE':
		user = User.query.filter_by(user_id=user_id).first()
		db.session.delete(user)
		db.session.commit()
		return jsonify({'user': user})
	else:
		return 'Delete user'


# Get Posts

@api.route('/posts', methods=['GET'])
def get_posts():
	posts = Post.query.all()
	return jsonify({'posts': post})

# Add post

@api.route('/posts', methods=['POST'])
def add_post():
	if request.method == 'POST':
		data = request.get_json()
		post = Post(title=data['title'], content=data['content'])
		#db.session.add(post)
		#db.session.commit()
		return jsonify({'data': data})
	else:
		return 'add a post'

# Get one post

@api.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
	post = Post.query.filter_by(id=post_id).first()
	return jsonify({'post': post})



# update one post

@api.route('/posts/<int:post_id>/update', methods=['PUT'])
def update_post(post_id):
	if request.method == 'PUT':
		post = Post.query.filter_by(id=post_id).first()
		data = request.get_json()
		post.title = data['title']
		post.content = data['content']
		db.session.commit()
		return jsonify({'post': post})



# Delete one post


@api.route('/posts/<int:post_id>/delete', methods=['DELETE'])
def delete_post(post_id):
	if request.method == 'DELETE':
		post = Post.query.filter_by(id=post_id).first()
		db.session.delete(post)
		db.session.commit()
		return jsonify({'post': post})
	else:
		return 'Delete a post'



# Get post words

# Get post sentences

# get post nouns

# get post verbs

# get post adjectives

# get post adverbs

# get post determiners

# get post synsets of each word 


# get comments

@api.route('/comments', methods=['GET'])
def get_comments():
	comments = Comment.query.all()
	return jsonify({'comments': comments})


# add comment

@api.route('/comments', methods=['POST'])
def add_comment():
	if request.method == 'POST':
		data = request.get_json()
		comment = Comment(comment=data['comment'], userid=data['userid'], postid=['postid'])
		db.session.add(comment)
		db.session.commit()
		return jsonify({"comment": comment})
	else:
		return "add comment"




# get one comment

@api.route('/comments/<int:comment_id>', methods=['GET'])
def get_comment(comment_id):
	comment = Comment.query.filter_by(comment_id=comment_id).first()
	return jsonify({'comment': comment})



# update one comment

@api.route('/comments/<int:comment_id>/update', methods=['PUT'])
def update_comment(comment_id):
	if request.method == 'PUT':
		comment = Comment.query.filter_by(comment_id=comment_id).first()
		data = request.get_json()
		comment.comment = data['comment']
		db.session.commit()
		return jsonify({'comment': comment})
	else:
		return 'Update a comment'


# delete one comment

@api.route('/comments/<int:comment_id>/delete', methods=['DELETE'])
def delete_comment(comment_id):
	if request.method == 'DELETE':
		comment = Comment.query.filter_by(comment_id=comment_id).first()
		db.session.delete(comment)
		db.session.commit()
		return jsonify({'comment': comment})
	else:
		return 'Delete a comment'
