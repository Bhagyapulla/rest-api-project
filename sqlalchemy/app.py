from flask import Flask
from models import Db

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

Db.init_app(app)

@app.route('/')
def home():
    return "Welcome to Flask-SQLALCHEMY!"

if __name__ == '__main__':
        app.run(debug=True)