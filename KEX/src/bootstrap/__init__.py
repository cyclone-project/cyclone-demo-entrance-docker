from flask import Flask

import os

from flask.ext.bootstrap import Bootstrap
from flask.ext.login import LoginManager
from flask.ext.mail import Mail
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.user import SQLAlchemyAdapter, UserManager

basedir = os.path.expanduser('~') + '/.kex/'

app = Flask(__name__)

app.config.from_object('config.default')
# app.config.from_object('config.production')

db = SQLAlchemy(app)
mail = Mail(app)
Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)

from models import User

db_adapter = SQLAlchemyAdapter(db, User)
user_manager = UserManager(db_adapter=db_adapter, app=app, login_manager=login_manager)

from keys import keys

app.register_blueprint(keys)

import views, oauth