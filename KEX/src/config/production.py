from bootstrap import basedir
import os

DEBUG = False
TESTING = False
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'kex.db')
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'kex.db')