import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Class model that config the database"""

    SQLALCHEMY_DATABASE_URI = \
            'sqlite:///' + os.path.join(basedir, 'post.db')
    SQLALCHEMY_POOL_RECYCLE = 299
    SECRET_KEY = 'XT\x9af\xc9\x8c\xf4\xaf\xf4\xc6\r\xd5\x91\x1e\xdc"| \x8e\xe9-\xc5\x86\xcb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
