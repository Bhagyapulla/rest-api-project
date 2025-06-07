from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy
# from models import db,Student
import os

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql:///site.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
app.config['UPLOAD_PATH']='static/images'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    file = request.files.get('file')
    file.save(os.path.join(app.config['UPLOAD_PATH'],file.filename))
    di={
        'name':name,'email':email,'phone':phone,'file':file
    }
    return render_template('second.html', **di)

if __name__ == '__main__':
    app.run(debug=True)