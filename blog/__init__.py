from flask import Flask
from config import Config
from blog.extensions import (
     db,
     ckeditor, 
     login_manager,
     mail,
     )
from blog.models.user import User
import os


def create_app(config_class=Config):
    """Method that configure the app"""
    app = Flask(__name__)
    app.config.from_object(config_class)

    # For flask extensions
    db.init_app(app)
    ckeditor.init_app(app)
    # oauth.init__app(app)
    
    # user_mixin.init_app(app)
    login_manager.login_view = 'post.blog'
    login_manager.init_app(app)
    #Configure flask-mail for sending emails
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASSWORD')

    # for mail activation
    mail.init_app(app)
    
    # Register Blurprints
    from blog.main import bp as main_bp
    app.register_blueprint(main_bp)

    from blog.post import bp as post_bp
    app.register_blueprint(post_bp)

    from blog.admin import bp as admin_bp
    app.register_blueprint(admin_bp)
    
    from blog.contact import bp as contact_bp
    app.register_blueprint(contact_bp)
    
    
    @login_manager.user_loader
    def load_user(user_id):
        """Find specific user that is store
        in the cookie session
        """
        return (User.query.get(int(user_id)))

    return (app)
