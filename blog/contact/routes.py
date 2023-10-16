from flask import render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
from blog.contact import bp
from blog.extensions import mail
from flask_mail import Message
import os


class ContactForm(FlaskForm):
    name = StringField('Name:', validators=[DataRequired()])
    email = StringField('Email:', validators=[DataRequired(), Email()])
    message = TextAreaField('Message:', validators=[DataRequired()])
    submit = SubmitField('Send')
    
    
@bp.route('/contact', methods=['GET', 'POST'])
def contact():
    """Method that handles the contact form"""
    form = ContactForm()
    
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data
        
        msg = Message(subject="New message from my blog website",
                      sender=email,
                      recipients = [os.environ.get('EMAIL_USERNAME')])
        
        msg.body = f'Name: {name}\nEmail: {email}\nMessage: {message}'
        
        mail.send(msg)
        
        flash('Your message has been sent!', 'success')
        return(redirect(url_for('contact.contact')))
    
    return(render_template('contact/contact.html', form=form))