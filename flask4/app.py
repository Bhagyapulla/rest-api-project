# # from crypt import methods
# #
# # from lib2to3.fixer_util import String
# # from pickle import FLOAT
# from crypt import methods
#
# from flask import Flask,render_template,redirect,url_for
# from forms import  HelloForm
#
# app = Flask(__name__)
#
# # @app.route('/',methods=['GET','POST'])
# # def index():
# #     form = NameForm()
# #     if form.validate_on_submit():
# #         name = form.username.data
# #         return f'hello,{name}!'
# #     return render_template('form_wtf.html',form=form)
# # if __name__ == '__main__':
# #     app.run(debug=True)
#
# # from flask import Flask, render_template ,redirect,url_for
# # from wtforms.validators import email
# #
# # from forms import LoginForm, ContactForm, FirstForm
# #
# # app = Flask(__name__)
# #
# #
# # @app.route('/login', methods=['GET', 'POST'])
# # def login():
# #     form = LoginForm()
# #     if form.validate_on_submit():
# #         username = form.username.data
# #         return f'Welcome, {username}!'
# #     return render_template('login.html', form=form)
# #
# # @app.route('/contact', methods=['GET', 'POST'])
# # def contact():
# #     form = ContactForm()
# #     if form.validate_on_submit():
# #         name = form.name.data
# #         email = form.email.data
# #         message = form.message.data
# #         return f'Thank you, {name}! Your message has been received.'
# #     return render_template('contact.html',form=form)
# #
# #
# #
# @app.route('/', methods=['GET', 'POST'])
# def register():
#     form = FirstForm()
#     if form.validate_on_submit():
#             name = form.name.data
#             middle_name = form.middle_name.data
#             last_name = form.last_name.data
#             email = form.email.data
#             return f"Welcome, {name} {middle_name} {last_name}!"
#
#     return render_template('form.html',form=form)
#

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/',methods=['GET','POST'])
def validator():
    form = HelloForm()
    if form.validate_on_submit():
        username = form.username.data
        return render_template('hello.html',username=username)
    return render_template('form.html',form=form)
if __name__ == '__main__':
     app.run(debug=True)