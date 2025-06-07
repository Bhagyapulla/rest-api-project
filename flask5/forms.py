
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class HelloForm(FlaskForm):
    name = StringField('Enter Your Name',validators=[DataRequired()])
    submit = SubmitField('Say Hello')
    class Meta:
        csrf = False