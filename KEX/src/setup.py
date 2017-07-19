from distutils.core import setup
from setuptools import find_packages

setup(
        name='KEX',
        version='1.0.0',
        packages=find_packages(),
        url='philip.raschke.cc',
        license='MIT',
        author='Philip Raschke',
        author_email='philip-raschke@mailbox.tu-berlin.de',
        description='Kex exchange service for the entrance project',
        install_requires=['Flask', 'flask-sqlalchemy', 'flask-bootstrap', 'flask-user', 'flask-mail', 'Flask-OAuthlib']
)