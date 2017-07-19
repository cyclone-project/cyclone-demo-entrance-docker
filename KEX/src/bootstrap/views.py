from flask import make_response
from flask.ext.user import login_required

from bootstrap import app


@app.route('/', methods=['GET'])
@login_required
def welcome():
    return make_response('KEX', 200)
