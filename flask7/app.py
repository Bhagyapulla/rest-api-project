from flask import  Flask,request

from flask_restful import Resource,Api

app  = Flask(__name__)
api = Api(app)

students = {}
class Student(Resource):
    def get(self,student_id):
        if student_id in students:
            return {student_id:students[student_id]}
        return {"error":"Student not found"},404
    def post(self,student_id):
        data = request.json
        if student_id in students:
            students[student_id].update(data)
            return {student_id:students[student_id]}
        else:
            students[student_id] = data
            return {student_id:data},201
    def delete(self,student_id):
        if student_id in students:
            del students[student_id]
            return {"messsge":f"Student {student_id} deleted "}
        return {'error':"Student not found"},404
api.add_resource(Student,'/student/<string:student_id>')

if __name__ == '__main__':
    app.run(debug=True)

