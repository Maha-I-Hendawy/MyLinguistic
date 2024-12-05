from project import app, db
from flask import Blueprint, render_template, request, redirect, url_for
from .models import Sentence
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk import pos_tag


tree = Blueprint('tree', __name__, template_folder='templates')



@tree.route('/sentences', methods=['GET', 'POST'])
def sentences():
	sentences = Sentence.query.all()
	if request.method == 'POST':
		text = request.form['text']
		sentence = Sentence(sentence=text)
		db.session.add(sentence)
		db.session.commit()
		return redirect(request.url)

	return render_template("tree/sentences.html", sentences=sentences)



@tree.route('/sentence/<int:sentence_id>')
def get_sentence(sentence_id):
	sentence = Sentence.query.filter_by(id=sentence_id).first()
	words = word_tokenize(sentence.sentence)
	for w in words:
		if w == '.' or w == ',':
			words.remove(w)
	tagged = pos_tag(words)

	if request.method == 'POST':
		word = request.form['word']
		pos = request.form['pos']
		
	return render_template("tree/get_sentence.html", words=words, tagged=tagged)