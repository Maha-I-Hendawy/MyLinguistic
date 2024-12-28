from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')


db = SQLAlchemy(app)

app.app_context().push()


from project.site.routes import site
from project.user.routes import user
from project.post.routes import mypost 
from project.tree.routes import tree
# from project.transcription.routes import transcription

app.register_blueprint(site)
app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(mypost, url_prefix='/post')
app.register_blueprint(tree, url_prefix='/tree')
# app.register_blueprint(transcription, url_prefix='/transcription')



