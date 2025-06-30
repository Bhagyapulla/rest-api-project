from flask_sqlalchemy import SQLAlchemy

Db = SQLAlchemy()

class Student(Db.Model):
    __tablename__ = 'student'
    id = Db.Column(Db.Integer, primary_key=True)
    name = Db.Column(Db.String(100))
    age = Db.Column(Db.Integer)