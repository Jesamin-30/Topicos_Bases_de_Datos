from numpy import dot
from numpy.linalg import norm
import numpy as np 

def stringtoList(text):
    vec=text.split(',')
    array=[]
    for i in range (0,len(vec)):
        array.append(float(vec[i]))
    return (array)

def ordenar(lista):
    tam=len(lista)
    for i in range(0,tam):
        for j in range(0,tam-i-1):
            if (lista[j][1]<lista[j+1][1]):
                temp=lista[j]
                lista[j]=lista[j+1]
                lista[j+1]=temp
    return lista

def calcular_coseno(matriz,selection):
    size = matriz.shape[0]
    lista=[]
    for i in range (0,size):
        if selection != i :
            cos_sim = dot(matriz[selection], matriz[i])/(norm(matriz[selection])*norm(matriz[i]))
            lista.append((i+1,cos_sim))
    return (ordenar(lista))


