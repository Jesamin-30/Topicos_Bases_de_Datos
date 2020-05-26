import sqlite3

def conectar():
    try:
        #sqliteConnection = sqlite3.connect('Bigramas/databasePartial.db') #6-16 20
        #sqliteConnection = sqlite3.connect('Bigramas/databaseComplete.db') # 50
        
        #sqliteConnection = sqlite3.connect('Bigramas/databasePartialIdx.db') #5-8
        sqliteConnection = sqlite3.connect('Bigramas/databaseCompleteIdx.db') #22

        print("Database created and Successfully Connected to SQLite")
        return sqliteConnection

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    