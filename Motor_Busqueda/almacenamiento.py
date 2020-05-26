from db import *
import time

keys_a = {}
keys_b = {}

bigrama = []
sqlite = conectar()
cursor = sqlite.cursor()

"""
Se crea las tablas necesarias en la base de datos sqlite
Hacemos uso del conector, con cursor ejecutamos querys en la base de datos
"""

def createTable():
	
	sql ='''CREATE TABLE KEYSA(
			WORD TEXT NOT NULL,
			ID_word INTEGER PRIMARY KEY
			)'''
	cursor.execute(sql)

	sql ='''CREATE TABLE KEYSB(
			WORD TEXT NOT NULL,
			ID_word INTEGER PRIMARY KEY
			)'''
	cursor.execute(sql)

	sql ='''CREATE TABLE BIGRAMA(
			ID_inicial INTEGER,
			ID_final INTEGER 
			)'''
	cursor.execute(sql)

	sql ='''CREATE TABLE INVERTED_INDEX(
			ID_inicial INTEGER PRIMARY KEY,
			terminos TEXT NOT NULL
			)'''
	cursor.execute(sql)

	sqlite.commit()


"""
Sql's para insertar 
	KeysA,
	KeysB,
	BIGRAMA,
	INVERTED_INDEX
"""

def insertarKeysA(tupla):
	sqlite_insert_query = '''INSERT INTO KEYSA
								(WORD, ID_word) 
								VALUES (?,?)'''
	cursor.execute(sqlite_insert_query,tupla)

def insertarKeysB(tupla):
	sqlite_insert_query = '''INSERT INTO KEYSB
								(WORD, ID_word) 
								VALUES (?,?)'''
	cursor.execute(sqlite_insert_query,tupla)

def insertarBigrama(tupla):
	sqlite_insert_query = '''INSERT INTO BIGRAMA
								(ID_inicial,ID_final) 
								VALUES (?,?)'''
	cursor.execute(sqlite_insert_query,tupla)

def insertarIndice(tupla):
	sqlite_insert_query = '''INSERT INTO INVERTED_INDEX
								(ID_inicial,terminos) 
								VALUES (?,?)'''
	cursor.execute(sqlite_insert_query,tupla)


"""
Aqui, se extrae los KEYSA, KEYSB por las dos columnas, secuencialmente también se va añadiendo la fila en la tabla
KEYSA, KEYSB, BIGRAMA
"""
def ponerID(filename,contador_a, contador_b):

	st = time.time()

	# Se lee el archivo preprocesado!!
	fileRead= open('Factorization/'+filename+'.fac','r')
	lines= fileRead.readlines()
	for l in lines:
		list=l.split()
		if (list[0] not in keys_a):
			keys_a[list[0]] = contador_a
			# Insertar keys in KEYSA si no se encuentra
			insertarKeysA((list[0],contador_a))
			contador_a+=1

		if (list[1] not in keys_b):
			keys_b[list[1]] = contador_b
			# Insertar keys in KEYSB si no se encuentra
			insertarKeysB((list[1],contador_b))
			contador_b+=1
		
		# Insertar una fila en la Tabla BIGRAMA por los KEYS ya encontrados
		insertarBigrama((keys_a[list[0]],keys_b[list[1]]))

	sqlite.commit()
	et = time.time()
	print('Time', filename, et-st)

	fileRead.close()
	return contador_a, contador_b


"""
En esta función, se agrupa todas las filas en la tabla BIGRAMA que 
comparten el mismo ID_inicial, se realiza con una query sql, el group by por ID_inicial, 

Y también se crea un indice en la tabla INVERTED_INDEX por el ID_inicial, para hacer la
busqueda aún un poco más rapida!!
"""
def invertedIndex():
	st = time.time()

	sqlite_inverted_query = '''INSERT INTO INVERTED_INDEX (ID_inicial, terminos) 
								SELECT ID_inicial, GROUP_CONCAT(ID_final)
								FROM BIGRAMA GROUP BY ID_inicial'''
								
	cursor.execute(sqlite_inverted_query)

	sqlite_index = '''CREATE UNIQUE INDEX IDX_INVERTED ON INVERTED_INDEX(ID_inicial)'''
	cursor.execute(sqlite_index)

	sqlite.commit()

	et = time.time()	
	print('Time Inverted', et-st)

	""" sqlite_select_query = 'SELECT * FROM BIGRAMA where ID_inicial = ?'

	print('\nTamaño keys', len(keys_a))
	count = 0
	for key in keys_a:

		#st = time.time()
		term = ''
		cursor.execute(sqlite_select_query,(keys_a[key],))
		row = cursor.fetchall()
		tam = len(row)
		for i in range(tam):
			if (i!=tam-1):
				term += str(row[i][1])+','
			else:
				term += str(row[i][1])
			
		insertarIndice((keys_a[key],term))
		#et = time.time()
		
		if(count%500 == 0):
			print('Time Inverted', count)

		count += 1

	sqlite.commit() """

if __name__ == "__main__":
	createTable()
	contador_a = 0
	contador_b = 0
	filenames = ['2gm-0000','2gm-0001','2gm-0002','2gm-0003','2gm-0004','2gm-0005','2gm-0006','2gm-0007','2gm-0008','2gm-0009',
            '2gm-0010','2gm-0011','2gm-0012','2gm-0013','2gm-0014','2gm-0015','2gm-0016','2gm-0017','2gm-0018','2gm-0019',
            '2gm-0020','2gm-0021','2gm-0022','2gm-0023','2gm-0024','2gm-0025','2gm-0026','2gm-0027','2gm-0028','2gm-0029',
            '2gm-0030','2gm-0031']
			
	for i in filenames:
		contador_a, contador_b =ponerID(i,contador_a, contador_b)
	
	invertedIndex()