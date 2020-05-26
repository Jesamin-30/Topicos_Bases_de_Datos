#export FLASK_APP=server.py
# flask run
from flask import Flask,render_template,request
import numpy as np 
from query import *

import time


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("search.html")


@app.route('/search',methods=['POST'])
def search():
    frase= request.form["palabra"]
    
    st = time.time()
    lista_result = query(frase)
    et = time.time()
    return render_template("result.html", lista=lista_result, tiempo=et-st)
    
    
