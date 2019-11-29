from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import EncryptedType
from sqlalchemy_utils.types.encrypted.encrypted_type import AesEngine

from emojikeygen import config

db = SQLAlchemy() 

class keys(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    emojikey = db.Column(db.String)
    name = db.Column(db.String)
    strategy = db.Column(db.String)
    date_created = db.Column(db.DateTime, server_default=db.func.now())
    key = db.Column(EncryptedType(db.Unicode, config.DATABASE_ENCRYPTION_KEY, AesEngine, 'pkcs5'))
