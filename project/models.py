from project import db
from datetime import datetime
#from marshmallow_sqlalchemy import SQLAlchemyAutoSchema






class User(db.Model):
	user_id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(100), nullable=False, unique=True)
	email = db.Column(db.String(100), nullable=False, unique=True)
	password = db.Column(db.String(100), nullable=False)
	#posts = db.relationship('Post', backref='user', lazy=True)
	#comments = db.relationship('Comment', backref='user', lazy=True)
	#sentences = db.relationship('Sentence', backref='user', lazy=True)


	def __repr__(self):
		return f"User({self.username}, {self.email})"



class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(200))
	content = db.Column(db.Text)
	image = db.Column(db.String(100))
	#date_created = db.Column(db.DateTime, default=datetime.utcnow)
	#userid = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)

	def __str__(self):
		return f"{self.title}, {self.image}"


"""

class PostSchema(ma.SQLAlchemyAutoSchema):
	class Meta:
		model = Post




post_schema = PostSchema()
posts_schema = PostSchema(many=True)


	
"""



class Comment(db.Model):
	comment_id = db.Column(db.Integer, primary_key=True)
	comment = db.Column(db.Text, nullable=False)
	date_created = db.Column(db.DateTime, default=datetime.utcnow)
	userid = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
	postid = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)


	def __repr__(self):
		return f"Comment('{self.comment}')"


"""



class CommentSchema(ma.SQLAlchemyAutoSchema):
	class Meta:
		model = Comment




comment_schema = CommentSchema()
comments_schema = CommentSchema(many=True)


"""

class Sentence(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	sentence = db.Column(db.String(200))
	user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)

	def __str__(self):
		return f"{self.sentence}"



"""

class SentenceSchema(ma.SQLAlchemyAutoSchema):
	class Meta:
		model = Sentence




sentence_schema = SentenceSchema()
sentences_schema = SentenceSchema(many=True)


"""
	