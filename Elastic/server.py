# export FLASK_APP=server.py


#!/usr/bin/env python3

from flask import Flask, request, render_template, redirect, url_for
from elasticsearch import Elasticsearch
import json

app = Flask(__name__)

elastic_client = Elasticsearch()

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/create', methods=['GET', 'POST'])
def create():
    if(request.method == 'GET'):
        return render_template("create.html")
    else:
   
        create_data = {
                "title": request.form["title"],
                "contenido": request.form["contenido"]
        }

        res = elastic_client.index(index='informacion',doc_type='articulo',body=create_data)
        print(res)

        return redirect(url_for('search'))


@app.route('/search', methods=['GET', 'POST'])
def search():
    if(request.method == 'GET'):
        return render_template("search.html")
    else:
        palabra = request.form["palabra"]
        
        search_param = {
            'query': {
                'match': {
                    'contenido': palabra
                }
            }
        }
        
        response = elastic_client.search(index="informacion", body=search_param)
        
        articulos = []
        for articulo in response["hits"]["hits"]:
            articulos.append(articulo["_source"])

        return render_template("list.html", articulos=articulos)
