from project import app, db
from flask import Blueprint, render_template, request, redirect, url_for
from markupsafe import escape
from werkzeug.utils import secure_filename
from .models import Post
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk import pos_tag
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk import WordNetLemmatizer
from nltk.corpus import wordnet


post = Blueprint('post', __name__, template_folder='templates')

# Stemming

stemmer1 = PorterStemmer()
stemmer2 = SnowballStemmer('english')

# Lemmatization

lemma = WordNetLemmatizer()



# Get All Posts

@post.route('/')
def post():
	posts = Post.query.all()
	return render_template("post.html", posts=posts)



# Create All Posts

@post.route('/upload', methods=['GET', 'POST'])
def upload():
	if request.method == 'POST':
		title = request.form['title']
		content = request.form['content']
		upload = request.files['upload']
		image = secure_filename(upload.filename)
		upload.save(f"project/static/images/{secure_filename(upload.filename)}")

		post = Post(title=title, content=content, image=image)
		db.session.add(post)
		db.session.commit()
		return redirect(url_for('home'))

	return render_template("upload.html", title="Post")


# Get One Post

@post.route('/post/<int:post_id>')
def get_post(post_id):
	post = Post.query.filter_by(id=post_id).first()
	return render_template('get_post.html', post=post, title="One Post")


# Update One Post

@post.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update_post(post_id):
	post = Post.query.filter_by(id=post_id).first()
	if request.method == 'POST':
		post.title = request.form['title']
		post.content = request.form['content']
		upload = request.files['upload']
		post.image = secure_filename(upload.filename)
		upload.save(f"project/static/images/{secure_filename(upload.filename)}")
		db.session.commit()
		return redirect(url_for("home"))

	return render_template("update_post.html", post=post, title="Update One Post")


# Delete One Post

@post.route('/delete/<int:post_id>')
def delete_post(post_id):
	post = Post.query.filter_by(id=post_id).first()
	db.session.delete(post)
	db.session.commit()
	return redirect(url_for("home"))


# Get a list of words and their parts of speech for one post

@post.route('/post/<int:post_id>/words')
def words(post_id):
	post = Post.query.filter_by(id=post_id).first()
	words = word_tokenize(post.content)
	for w in words:
		if w == '.' or w == ';' or w == ':' or w == '?' or w == '!' or w == ',':
			words.remove(w)
	tagged = pos_tag(words, tagset='universal')
	tagged1 = pos_tag(words)
	return render_template("words.html", tagged=tagged, title="Words")


# Get A list of sentences for one post

@post.route('/post/<int:post_id>/sents')
def sents(post_id):
	post = Post.query.filter_by(id=post_id).first()
	sents = sent_tokenize(post.content)
	return render_template("sents.html", sents=sents, title="Sentences")


# Get a list of verbs and their tenses from one post

@post.route('/post/<int:post_id>/verbs')
def get_verbs(post_id):
	post = Post.query.filter_by(id=post_id).first()
	words = word_tokenize(post.content)
	for w in words:
		if w == '.' or w == ';' or w == ':' or w == '?' or w == '!' or w == ',':
			words.remove(w)
	tagged = pos_tag(words)
	# get the base form of each verb in a text
	VBb = [lemma.lemmatize(w[0], 'v') for w in tagged if w[1] == 'VB']
	VBPb = [lemma.lemmatize(w[0], 'v') for w in tagged if w[1] == 'VBP']
	VBZb = [lemma.lemmatize(w[0], 'v') for w in tagged if w[1] == 'VBZ']
	VBGb = [lemma.lemmatize(w[0], 'v') for w in tagged if w[1] == 'VBG']
	VBDb = [lemma.lemmatize(w[0], 'v') for w in tagged if w[1] == 'VBD']
	VBNb = [lemma.lemmatize(w[0], 'v') for w in tagged if w[1] == 'VBN']
	return render_template("verbs.html", tagged=tagged, VBb=VBb, VBPb=VBPb, VBZb=VBZb, VBGb=VBGb, VBDb=VBDb, VBNb=VBNb, title="Sentences")


# Get a list of nouns from one post

@post.route('/post/<int:post_id>/nouns')
def nouns(post_id):
	post = Post.query.filter_by(id=post_id).first()
	words = word_tokenize(post.content)
	for w in words:
		if w == '.' or w == ';' or w == ':' or w == '?' or w == '!' or w == ',':
			words.remove(w)
	tagged = pos_tag(words)
	return render_template("nouns.html", tagged=tagged, title="Nouns")



# Get a list of adjectives from one post 


@post.route('/post/<int:post_id>/adjectives')
def adjectives(post_id):
	post = Post.query.filter_by(id=post_id).first()
	words = word_tokenize(post.content)
	for w in words:
		if w == '.' or w == ';' or w == ':' or w == '?' or w == '!' or w == ',':
			words.remove(w)
	tagged = pos_tag(words)
	return render_template("adjectives.html", tagged=tagged, title="Adjectives")


# Get a list of adverbs of one post

@post.route('/post/<int:post_id>/adverbs')
def adverbs(post_id):
	post = Post.query.filter_by(id=post_id).first()
	words = word_tokenize(post.content)
	for w in words:
		if w == '.' or w == ';' or w == ':' or w == '?' or w == '!' or w == ',':
			words.remove(w)
	tagged = pos_tag(words)
	return render_template("adverbs.html", tagged=tagged, title="Adverbs")


# Get a list of determiners from one post 

@post.route('/post/<int:post_id>/determiners')
def determiners(post_id):
	post = Post.query.filter_by(id=post_id).first()
	words = word_tokenize(post.content)
	for w in words:
		if w == '.' or w == ';' or w == ':' or w == '?' or w == '!' or w == ',':
			words.remove(w)
	tagged = pos_tag(words)
	return render_template("determiners.html", tagged=tagged, title="Determiners")



# Get a list of synonyms for each word of one post

@post.route('/post/<int:post_id>/synsets')
def synsets(post_id):
	post = Post.query.filter_by(id=post_id).first()
	words = word_tokenize(post.content)
	for w in words:
		if w == '.' or w == ';' or w == ':' or w == '?' or w == '!' or w == ',':
			words.remove(w)
	synsets = [wordnet.synsets(w) for w in words]
	for w in synsets:
		if w == []:
			synsets.remove(w)
	return render_template("synonym.html", synsets=synsets, title="Synonym")


