from flask import Blueprint

bp = Blueprint('contact', __name__)

from blog.contact import routes
