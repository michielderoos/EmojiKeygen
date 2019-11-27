from app import db

class keys(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, server_default=db.func.now())
