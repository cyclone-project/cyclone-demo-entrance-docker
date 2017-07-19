from bootstrap.models import Ext

from bootstrap import db


class KeyPair(db.Model, Ext):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.Text, nullable=False, unique=True) # gives information about the receiver of the secret key
    secret_key = db.Column(db.Text, nullable=False) # the actual secret key
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) # gives information about the author of the secret key

    def __init__(self, email, secret_key, user_id):
        self.email = email
        self.secret_key = secret_key
        self.user_id = user_id