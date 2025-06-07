# from flask import Flask,render_template
#
# app = Flask(__name__)
# @app.route('/book/')
# def addbook():
#     return render_template('addbook.html')
# @app.route('/')
# def add():
#
#     di=[{'Tittle':'on the Road','Author':'Jack Kerouac','Read':'Yes'},
#         {'Tittle':'harry potter and the philospher stone','Author':'j.k rowlling','Read':'no'},
#         {'Tittle':'Green eggs and Ham', 'Author': 'Dr.seuss', 'Read': 'Yes'}
#         ]
#     return render_template('book.html',di=di)
#
#
# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('registration.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    return redirect(url_for('welcome', username=username))

@app.route('/welcome')
def welcome():
    username = request.args.get('username')
    return render_template('first.html', username=username)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)

