from flask import Flask,render_template,request
from lem_stem import *
from coseno_2Vectores import *
import numpy as np 


app = Flask(__name__)

@app.route('/lematization_stemming')
def index_lem_stemm():
    return render_template("lem_stemm.html")

@app.route('/lematization_stemming',methods=['POST'])
def lema_stemm():
    frase= request.form["text"]
    
    if(request.form["action"]=="lema"):
        print(request.form["action"])
        return render_template("lem_stemm.html", frase=lematization(frase),inicial=frase)
        
    else:
        print(request.form["action"])  
        return render_template("lem_stemm.html",frase=stemming(frase),inicial=frase)
        
@app.route('/vector_space')
def index_coseno():
    return render_template("vector_space.html")

@app.route('/vector_space',methods=['POST'])
def comparacion():
    vect1=request.form["0"]
    vect2=request.form["1"]
    vect3=request.form["2"]
    vect4=request.form["3"]
    vect5=request.form["4"]

    a=stringtoList(vect1)
    b=stringtoList(vect2)
    c=stringtoList(vect3)
    d=stringtoList(vect4)
    e=stringtoList(vect5)

    matriz = np.array([a, b, c, d, e])
    lista=calcular_coseno(matriz,int(request.form["select"]))
    return render_template("vector_space.html", lista=lista,vect1=vect1,vect2=vect2,vect3=vect3,vect4=vect4,vect5=vect5)