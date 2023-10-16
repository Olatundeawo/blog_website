from flask import render_template,request, redirect, url_for
from blog.post import bp
from blog.models.post import Post
from blog.extensions import db
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired
from flask_ckeditor import CKEditorField
from datetime import datetime
import re



class EditPost(FlaskForm):
    """Class for editing a post"""
    heading = StringField('heading', validators=[DataRequired()])
    post = CKEditorField('post', validators=[DataRequired()])


@bp.route('/blog')
def blog():
    """ Blog route"""
    headings = Post.query.all()
    date_posted = Post.post_date
    return (render_template('blog/blog.html', headings=headings, date_posted=date_posted))


def speed_count(article_post):
    """Method that estimate the reading time"""
    words = re.findall(r'\w+', article_post)
    word_count = len(words)
    speed = 200
    average_speed = word_count / speed
    return (round(average_speed))



@bp.route('/blog<string:title>')
def get_post(title):
    """get the blog post by heading"""
    blog_post = Post.query.filter_by(heading=title).first()
    if blog_post:
        reading_time = speed_count(blog_post.post)
        return (render_template('blog/blog_post.html', post=blog_post, reading_time=reading_time ))
    else:
        return 'Blog post not found', 404



@bp.route('/edit<int:post_id>', methods=['POST', 'GET'])
def edit_post(post_id):
    """Method to edit a post"""
    post = Post.query.filter_by(id=post_id).first()
    
    form = EditPost()
    
    if request.method == 'POST' and form.validate_on_submit():
        post.heading = form.heading.data
        post.post = form.post.data
        db.session.commit()
        return(redirect(url_for('post.blog')))
    
    form.heading.data = post.heading
    form.post.data = post.post
    
    return (render_template('blog/edit.html', form=form, post=post))


@bp.route('/blog<string:title>', methods=['POST', 'DELETE'])
def delete_post(title):
    """Method for deleteing a post"""
    blog_post = Post.query.filter_by(heading=title).first()
    if request.method == 'POST':
        
        db.session.delete(blog_post)
        db.session.commit()
        return (redirect(url_for('post.blog')))
    
