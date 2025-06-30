from dbm import error

from flask import Flask, request
from flask_restful import Api,Resource

app = Flask(__name__)

api = Api(app)

books = [
    {"id":1,"title":"concept of Physics","author":"H>C Verma"},
    {"id":2,"title":"Gunahon ka Devta","author":"Dharmavir"},
    {"id":3,"title":"problems in general physics","author":"I.E Irodov"}

]

class BookResource(Resource):
    def get(self,book_id=None):
        if book_id is None:
            return books,200
        book = next((book for book in books if book["id"]==book_id),None)
        if book:
            return book,200
        return {"error":"Book not found"},404
    def post(self):
        new_book=request.json
        books.append(new_book)
        return new_book,201
    def put(self,book_id):
        book = next((book for book in books if book["id"]==book_id),None)
        if not book:
            return {"error":"Books not found"},404
        data= request.json
        book.update(data)
        return book,200
    def delete(self,book_id):
        global books
        books= [book for book in books if book["id"]!=book_id]
        return {'message':"Book Deleted"},200
api.add_resource(BookResource,'/books','/books/<int:book_id>')

if __name__ == '__main__':
    app.run(debug=True)
