from flask import render_template
from blog.main import bp


@bp.route('/')
def about():
    """ Display the about page
        which is the index page
    """
    return(render_template('about.html'))

