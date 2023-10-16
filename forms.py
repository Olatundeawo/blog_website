from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, IntegerField)
from wtforms.validators import InputRequired, Length


class Post(FlaskForm):
    heading = StringField('Title', validators = [InputRequired(),
                                               Length(min=10, max=100)])
    
    post = TextAreaField('Text',
                                validators=[InputRequired(),
                                            Length(max=200)])