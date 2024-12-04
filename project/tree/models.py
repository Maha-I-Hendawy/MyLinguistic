from project import db





class Sentence(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	sentence = db.Column(db.String(200))

	def __str__(self):
		return f"{self.sentence}"


		
