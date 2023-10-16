from blog.extensions import db
from flask_login import UserMixin
from datetime import datetime

class Post(UserMixin, db.Model):
    """ Define a post model """
    id = db.Column(db.Integer, primary_key=True)
    heading = db.Column(db.String(100), nullable=False)
    post = db.Column(db.String(100))
    post_date = db.Column(db.DateTime, default=datetime.utcnow)
