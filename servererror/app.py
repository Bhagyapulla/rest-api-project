from zipapp import ZipAppError

from flask import Flask,request,jsonify
import time

from select import error

app=Flask(__name__)

@app.before_request



def before_request_func():
    request.start_time=time.time()
    print(f"[Middleware]Before request:{request.method}{request.path}")

@app.after_request
def after_request_func(response):
    duration=time.time()-request.start_time
    print(f"[Middleware]After request: {request.method} {request.path} took {duration:.4f}s")
    return response

@app.route('/')

def index():
    return "Hello,Flask!"

@app.route('/divide')

def divide():
    a=int(request.args.get("a",1))
    b=int(request.args.get("b",0))
    return jsonify(result=a/b)

@app.errorhandler(ZipAppError)
def handle_zero_division_error(e):
    return jsonify(error="Cannot divide by zero!"),400

@app.errorhandler(404)
def handle_404_error(e):
    return jsonify(error="Page not found! "),404

@app.errorhandler(Exception)
def handle_generic_error(e):
    print(f"[Error]{e}")
    return jsonify(error="Something went wrong!"),500

if __name__ == '__main__':
    app.run(debug=True)
