


class Student(db.models):
    id = db.Column(db.Integer,primary_key=True)
    name= db.Column(db.String(100))
    marks = db.Column(db.Integer)

    def __repr__(self):
        return f"<Student {self.name}>"



