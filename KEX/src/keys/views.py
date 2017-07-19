import json

from flask import make_response, request
from flask.ext.login import current_user
from flask.ext.user import login_required
from bootstrap.models import User
from bootstrap import db
from keys import keys
from keys.models import KeyPair


@keys.route('', methods=['POST'])
@login_required
def push_key():
    # to push a secret key to the KEX
    data = json.JSONDecoder().decode(request.data)
    if 'email' not in data or 'secret_key' not in data:
        return make_response('', 400) # error missing parameter

    keypair = KeyPair.query.filter_by(email=data['email'], user_id=current_user.id).first() # load key pair if existent
    if keypair is None:
        keypair = KeyPair(data['email'], data['secret_key'], current_user.id) # otherwise instantiate
    else:
        keypair.secret_key = data['secret_key'] # else override old secret key
    db.session.add(keypair)
    db.session.commit()

    return make_response('', 200) # inform about success


@keys.route('/<owner>', methods=['GET'])
@login_required
def fetch_key(owner):
    # to fetch a secret key from the KEX
    owner = User.query.filter_by(email=owner).first_or_404() # if existent ...
    # ... load secret key for authenticated user that has been authored by owner
    keypair = KeyPair.query.filter_by(email=current_user.email, user_id=owner.id).first_or_404()
    return make_response(keypair.secret_key, 200)
