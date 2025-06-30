from fileinput import lineno
from time import asctime

from flask import Flask,request,jsonify
import logging
from middleware import RequestTimerMiddleware

logging.basicConfig(filename='app.log',level=logging.ERROR),
    format=%asctime()s %(levelname)s:%(message)s.[in %(in %(pathname)s%(lineno))d]')

app=Flask(__name__)

app.wsgi_app=requestTimerMiddleware(app.wsgi_app)

@app.route('/')
def home():
    return "welcome to flask with Middleware"

@app.errorhandler(ZeroDivisionError)
