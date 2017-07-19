from flask import Blueprint

keys = Blueprint('keys', __name__, static_folder='static', template_folder='templates', url_prefix='/keys')

import views