from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from emojikeygen.resources.shorten import Shorten

# Create app, load config
app = Flask(__name__)
app.config.from_pyfile("config.py")

# Set up database
db = SQLAlchemy()
db.init_app(app)
with app.app_context():
    db.create_all()

# Create routes
api = Api(app)
api.add_resource(Shorten, '/emojikey', '/emojikey/<string:emojikey>')

