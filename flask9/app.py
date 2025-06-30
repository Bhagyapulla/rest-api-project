# from crypt import methods

from flask import Flask, request, jsonify
# from flask_restful import Api,Resource

app = Flask(__name__)

# api = Api(app)

books = [
    {"id":1,"title":"concept of Physics","author":"H>C Verma"},
    {"id":2,"title":"Gunahon ka Devta","author":"Dharmavir"},
    {"id":3,"title":"problems in general physics","author":"I.E Irodov"}

]

@app.route('/books',methods=['GET'])
def get_books():
    return jsonify(books)
@app.route('/books/<int:book_id>',methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    return jsonify(book)if book else (jsonify({"error":"Book not found"}),404)
@app.route('/books',methods=['POST'])
def add_book():
    new_book=request.json
    books.append(new_book)
    return jsonify(new_book),201
@app.route('/books/<int:book_id>',methods=['PUT'])
def update_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if not book:
       return jsonify({"error": "Book not found"}), 404
    data=request.json
    book.update(data)
    return jsonify(book)
@app.route('/books/<int:book_id>',methods=['DELETE'])
def delete_book(book_id):
    global books
    books=[book for book in books if book["id"]!=book_id]
    return jsonify ({"message": "Book deleted"})

if __name__ == '__main__':
    app.run(debug=True)