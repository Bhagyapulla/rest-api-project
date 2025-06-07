# from sqlalchemy.dialects.mssql.information_schema import tables
# from sqlalchemy.sql.ddl import CreateTable
#
#
# class Student(db.models):
#     id = db.Column(db.Integer,primary_key=True)
#     name= db.Column(db.String(100))
#     marks = db.Column(db.Integer)
#
#     def __repr__(self):
#         return f"<Student {self.name}>"
# Create tables
# with app.app_context():
#     db.create_all()