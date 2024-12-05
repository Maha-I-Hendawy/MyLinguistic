from project import db
from project.post.models import Post



class User(db.Model):
	user_id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(100), nullable=False, unique=True)
	email = db.Column(db.String(100), nullable=False, unique=True)
	password = db.Column(db.String(100), nullable=False)
	#post = db.relationship('Post', backref='user', lazy=True)



	def __str__(self):
		return f"{self.username}, {self.email}"
