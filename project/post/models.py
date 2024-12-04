from project import db


class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(200))
	content = db.Column(db.Text)
	image = db.Column(db.String(100))

	def __str__(self):
		return f"{self.title}, {self.image}"




		
