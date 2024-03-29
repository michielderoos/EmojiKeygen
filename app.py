from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from emojikeygen.models import db, keys
from emojikeygen.resources.shorten import Shorten

# Create app, load config
app = Flask(__name__)
app.config.from_pyfile("emojikeygen/config.py")

# Set up database
db.init_app(app)
with app.app_context():
	db.create_all()

# Create routes
api = Api(app)
CORS(app)
api.add_resource(Shorten, '/emojikey', '/emojikey/<string:emojikey>')

if __name__ == '__main__':
	app.run(debug=True)

