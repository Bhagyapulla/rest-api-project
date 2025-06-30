from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField ,PasswordField,TextAreaField
from wtforms.fields import EmailField
from wtforms.validators import DataRequired, Email

class HelloForm(FlaskForm):
    username = StringField('Enter Your Name',validators=[DataRequired()])
    submit = SubmitField('Say Hello')
    class Meta:
        csrf = False

# class LoginForm(FlaskForm):
#     username = StringField('Name')
#     password = PasswordField('password')
#     submit = SubmitField('submit')
#     class Meta:
#         csrf = False
#
# class ContactForm(FlaskForm):
#     name = StringField('name')
#     email = StringField('email',validators=[DataRequired(), Email()])
#     message = TextAreaField('message')
#     submit = SubmitField('submit')
#     class Meta:
#         csrf = False
#
# class FirstForm(FlaskForm):
#     name = StringField('First Name')
#     middle_name = StringField('Middle Name')
#     last_name = StringField('Last Name')
#
#     email = EmailField('Email',validators=[DataRequired(), Email()])
#     submit = SubmitField('Submit')
#     class Meta:
#         csrf = False