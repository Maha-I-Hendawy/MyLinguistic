from project import app, db
from flask import Blueprint, render_template, request, redirect, url_for
from markupsafe import escape
from werkzeug.utils import secure_filename
from project.models import Post
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk import pos_tag
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk import WordNetLemmatizer
from nltk.corpus import wordnet
from project.user.routes import * 


mypost = Blueprint('post', __name__, template_folder='templates')

# Stemming

stemmer1 = PorterStemmer()
stemmer2 = SnowballStemmer('english')

# Lemmatization

lemma = WordNetLemmatizer()



# Get All Posts

@mypost.route('/')
def all_posts():
	if 'user' in session:
		posts = Post.query.all()
		return render_template("post/post.html", posts=posts)
	else:
		return redirect(url_for('user.login'))
	


# Create All Posts

@mypost.route('/post', methods=['GET', 'POST'])
def add_post():
	if 'user' in session:
		if request.method == 'POST':
			title = request.form['title']
			content = request.form['content']
			upload = request.files['upload']
			image = secure_filename(upload.filename)
			upload.save(f"project/static/images/{secure_filename(upload.filename)}")

			post = Post(title=title, content=content, image=image)
			db.session.add(post)
			db.session.commit()
			return redirect(url_for('post.post'))
		return render_template("post/upload.html", title="Post")

	else:
		return redirect(url_for('user.login'))
	


	
# Get One Post

@mypost.route('/post/<int:post_id>')
def get_post(post_id):
	if 'user' in session:
		post = Post.query.filter_by(id=post_id).first()
		return render_template('post/get_post.html', post=post, title="One Post")

	else:
		return redirect(url_for('user.login'))
	

# Update One Post

@mypost.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update_post(post_id):
	if 'user' in session:
		post = Post.query.filter_by(id=post_id).first()
		if request.method == 'POST':
			post.title = request.form['title']
			post.content = request.form['content']
			upload = request.files['upload']
			post.image = secure_filename(upload.filename)
			upload.save(f"project/static/images/{secure_filename(upload.filename)}")
			db.session.commit()
			return redirect(url_for("post.post"))
		return render_template("post/update_post.html", post=post, title="Update One Post")
	else:
		return redirect(url_for('user.login'))
	


# Delete One Post

@mypost.route('/delete/<int:post_id>')
def delete_post(post_id):
	if 'user' in session:
		post = Post.query.filter_by(id=post_id).first()
		db.session.delete(post)
		db.session.commit()
		return redirect(url_for("post.post"))
	else:
		return redirect(url_for('user.login'))

	


# Get a list of words and their parts of speech for one post

@mypost.route('/post/<int:post_id>/words')
def words(post_id):
	if 'user' in session:

		post = Post.query.filter_by(id=post_id).first()
		words = word_tokenize(post.content)
		for w in words:
			if w == '.' or w == ';' or w == ':' or w == '?' or w == '!' or w == ',':
				words.remove(w)
		tagged = pos_tag(words, tagset='universal')
		tagged1 = pos_tag(words)
		return render_template("tokenize/words.html", tagged=tagged, title="Words")

	else:
		return redirect(url_for('user.login'))


# Get A list of sentences for one post

@mypost.route('/post/<int:post_id>/sents')
def sents(post_id):
	if 'user' in session:
		post = Post.query.filter_by(id=post_id).first()
		sents = sent_tokenize(post.content)
		return render_template("tokenize/sents.html", sents=sents, title="Sentences")
	else:
		return redirect(url_for('user.login'))

# Get a list of verbs and their tenses from one post

@mypost.route('/post/<int:post_id>/verbs')
def get_verbs(post_id):
	if 'user' in session:

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
		return render_template("pos/verbs.html", tagged=tagged, VBb=VBb, VBPb=VBPb, VBZb=VBZb, VBGb=VBGb, VBDb=VBDb, VBNb=VBNb, title="Sentences")
	else:
		return redirect(url_for('user.login'))

# Get a list of nouns from one post

@mypost.route('/post/<int:post_id>/nouns')
def nouns(post_id):
	if 'user' in session:
		post = Post.query.filter_by(id=post_id).first()
		words = word_tokenize(post.content)
		for w in words:
			if w == '.' or w == ';' or w == ':' or w == '?' or w == '!' or w == ',':
				words.remove(w)
		tagged = pos_tag(words)
		return render_template("pos/nouns.html", tagged=tagged, title="Nouns")
	else:
		return redirect(url_for('user.login'))

# Get a list of adjectives from one post 


@mypost.route('/post/<int:post_id>/adjectives')
def adjectives(post_id):
	if 'user' in session:

		post = Post.query.filter_by(id=post_id).first()
		words = word_tokenize(post.content)
		for w in words:
			if w == '.' or w == ';' or w == ':' or w == '?' or w == '!' or w == ',':
				words.remove(w)
		tagged = pos_tag(words)
		return render_template("pos/adjectives.html", tagged=tagged, title="Adjectives")
	else:
		return redirect(url_for('user.login'))
# Get a list of adverbs of one post

@mypost.route('/post/<int:post_id>/adverbs')
def adverbs(post_id):
	if 'user' in session:

		post = Post.query.filter_by(id=post_id).first()
		words = word_tokenize(post.content)
		for w in words:
			if w == '.' or w == ';' or w == ':' or w == '?' or w == '!' or w == ',':
				words.remove(w)
		tagged = pos_tag(words)
		return render_template("pos/adverbs.html", tagged=tagged, title="Adverbs")
	else:
		return redirect(url_for('user.login'))
# Get a list of determiners from one post 

@mypost.route('/post/<int:post_id>/determiners')
def determiners(post_id):
	if 'user' in session:

		post = Post.query.filter_by(id=post_id).first()
		words = word_tokenize(post.content)
		for w in words:
			if w == '.' or w == ';' or w == ':' or w == '?' or w == '!' or w == ',':
				words.remove(w)
		tagged = pos_tag(words)
		return render_template("pos/determiners.html", tagged=tagged, title="Determiners")
	else:
		return redirect(url_for('user.login'))


# Get a list of synonyms for each word of one post

@mypost.route('/post/<int:post_id>/synsets')
def synsets(post_id):
	if 'user' in session:

		post = Post.query.filter_by(id=post_id).first()
		words = word_tokenize(post.content)
		for w in words:
			if w == '.' or w == ';' or w == ':' or w == '?' or w == '!' or w == ',':
				words.remove(w)
		synsets = [wordnet.synsets(w) for w in words]
		for w in synsets:
			if w == []:
				synsets.remove(w)
		return render_template("wordnet/synonym.html", synsets=synsets, title="Synonym")
	else:
		return redirect(url_for('user.login'))
