from db import *


"""
Se ectrae los KEYSA de la base de datos!
"""
def extraer_keys(cursor,palabras):
    sqlite_select_query = 'SELECT * FROM KEYSA'
    cursor.execute(sqlite_select_query)
    row = cursor.fetchall()

    for i in row:
        palabras[i[1]] = i[0]
"""
Se busca la palabra en el diccionario y se obtiene el ID de la palabra
Si no, retorna -1 y no se encuentra esa palabra!!
"""
def retornar_indice(palabra,palabras):
    for i in palabras:
        if (palabras[i] == palabra):
            return i
    return -1

"""
Función para hacer las consultas por una palabra!!
"""

def query(word):
    sqlite = conectar()
    cursor = sqlite.cursor()
    palabras = {}
    ranking = {}

    extraer_keys(cursor,palabras)
    indice_palabra = retornar_indice(word,palabras)
    if(indice_palabra >= 0):
        
        sqlite_existe_query = 'SELECT terminos FROM INVERTED_INDEX where ID_inicial = ?'
        cursor.execute(sqlite_existe_query,(indice_palabra,))
        list_terminos = cursor.fetchall()
        
        
        if (list_terminos == []):
            return [(-1,'No es ID inicial')]
        
        else:
            cursor.execute('SELECT ID_inicial FROM INVERTED_INDEX')
            list_id = cursor.fetchall()
            a = set(list_terminos[0][0].split(',')) 
            for i in list_id:

                # Buscamos el conjunto a comparar que tenga el ID_inicial = 1,2,3,4,5,6,7.....
                cursor.execute('SELECT terminos FROM INVERTED_INDEX where ID_inicial = ?',(i[0],))

                list_termB = cursor.fetchall()

                b = set(list_termB[0][0].split(',')) 

                """
                    Similitud con Jaccard!!
                    Se calcula la division del tamaño que hace interseccion entre tamaño de la union de los dos conjuntos
                """
                similitud = len(a.intersection(b))/len(a.union(b))
                ranking[palabras[i[0]]] = similitud
            
            tmp = sorted(ranking.items(), key =lambda x: x[1], reverse=True)

            return tmp[:100]
    else:
        return [(-1,'No existe la palabra en el Corpus')]
                
""" if __name__ == "__main__":
    extraer_keys()
    query('trouble')
    palabras.clear() """
    

