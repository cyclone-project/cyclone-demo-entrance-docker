from bootstrap import basedir
import os

DEBUG = True
TESTING = False
SECRET_KEY = 'v\xfcB\xdc\xe1\xf6\xbc,\xe8Z\xfd\x9bE\x9b\xf9;@\x8e\xcd\xbb\xb2\xcc\xb8@'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'kex.dev.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

USER_APP_NAME = 'KEX'
USER_AFTER_LOGIN_ENDPOINT = 'welcome'
CSRF_ENABLED = False

MAIL_USERNAME = 'entrance.project.tu@gmail.com'
MAIL_PASSWORD = 'GUb78EpuJOHS8vUvvI8kkECG'
MAIL_DEFAULT_SENDER = 'entrance.project.tu@gmail.com'
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TLS = False

OAUTH2_PROVIDER_TOKEN_EXPIRES_IN = 31536000
