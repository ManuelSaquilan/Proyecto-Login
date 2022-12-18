import sqlite3

conn=sqlite3.connect("BaseDeDatos.db")
cursor=conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,username VARCHAR(50) NOT NULL,email VARCHAR(50) NOT NULL, nacimiento VARCHAR(50) NOT NULL, password VARCHAR(40) NOT NULL)""")

def savedata(username,email,nacimiento,password):
    cursor.execute("""INSERT INTO usuarios VALUES (NULL,?,?,?,?)""",(username,email,nacimiento,password))
    conn.commit()
    
def login(username, password):
    cursor.execute("""SELECT * FROM usuarios WHERE username=? AND password=? """,(username, password))
    if cursor.fetchone() is not None:
        return True
    else:
        return False