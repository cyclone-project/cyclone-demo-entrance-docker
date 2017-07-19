from bootstrap import basedir
import os

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'kex.test.db')