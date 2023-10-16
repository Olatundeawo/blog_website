from blog.admin import bp
from flask import render_template, redirect, request, url_for, flash
from blog.models.post import Post
from blog.extensions import db
from blog.models.user import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user


@bp.route('/admin/signup')
def signup():
    """signup method"""
    return (render_template('admin/signup.html'))


@bp.route('/admin/signup', methods=['GET', 'POST'])
def signup_post():
    """Method that save the admin details
        to the database
    """
    if request.method == "POST":
        
        email = request.form['email']
        password = request.form['password']
        name = request.form['name']
    
        user = User.query.filter_by(email=email).first()
    
        if user:
            flash('Email already registered!!!')
            return redirect(url_for('admin.signup'))
    
        new_user = User(email=email,
                    password=generate_password_hash(password, method='sha256'), name=name)
    
        db.session.add(new_user)
        db.session.commit()
        
    return (redirect(url_for('admin.login')))



@bp.route('/admin')
def login():
    """Loginin method"""
    return (render_template('admin/login.html'))


@bp.route('/admin', methods=['GET', 'POST'])
def login_post():
    """method that handle admin login"""
   
    email = request.form['email']
    password = request.form['password']
    remember = True 
    
    user = User.query.filter_by(email=email).first()
    
    if not user or not check_password_hash(user.password, password):
        flash("Email or password not correct")
        return (redirect(url_for('admin.login')))
    login_user(user, remember=remember)
    return (redirect(url_for('admin.admin')))



@bp.route('/admin/post', methods=['GET', 'POST'])
@login_required
def admin():
    """admin route that add post to the database"""

    if request.method == 'POST':
        post = request.form['ckeditor']

        headline = request.form['headline']


        new_post = Post(heading=headline, post=post)
        db.session.add(new_post)
        db.session.commit()
        return (redirect(url_for('main.about')))
    
    return (render_template('admin/admin.html'))


@bp.route('/admin/logout')
@login_required
def logout():
    """Method for logout"""
    logout_user()
    return (redirect(url_for('post.blog')))