import datetime
from bootstrap import basedir, db
from bootstrap.models import Client, User
import os

if not os.path.exists(basedir):
    os.makedirs(basedir)

open(basedir+'kex.db', 'w')
open(basedir+'kex.dev.db', 'w')
open(basedir+'kex.test.db', 'w')

db.create_all()

# register UM/CM component
# to enable OAuth authentication
umcm = Client(
    name='entrance UM/CM',
    description='User-management and Container-management component of entrance',
    client_id='QlWDSSGCCUFdD9Nupq3vA6Q7C95IQf2LjCqwBh10',
    client_secret='0Bh761e9WKEPkuyxPRMChey0d2m1uVkvDn20WyDum0Bb7TGUtt',
    is_confidential=True,
    _redirect_uris='/',
    _default_scopes=''
)
db.session.add(umcm)
db.session.commit()

user = User(
    username='philip',
    password='$2a$12$Z7La7sHfucFWEAGdjtO5re7wewDVp7IhyEdHyXzlQMYZ4KTOGKXNC',
    email='philip.raschke@outlook.com',
    confirmed_at= datetime.datetime.now(),
    active=True,
)
db.session.add(user)
db.session.commit()