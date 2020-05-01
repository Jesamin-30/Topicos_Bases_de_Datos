from flask import Flask,render_template,request
from lem_stem import *


app = Flask(__name__)

@app.route('/lematization_stemming')
def index():
    return render_template("lem_stemm.html")

@app.route('/lematization_stemming',methods=['POST'])
def lematizar():
    
    frase= request.form["text"]
    
    if(request.form["action"]=="lema"):
        print(request.form["action"])
        return render_template("lem_stemm.html", frase=lematization(frase),inicial=frase)
        
    else:
        print(request.form["action"])  
        return render_template("lem_stemm.html",frase=stemming(frase),inicial=frase)
        

