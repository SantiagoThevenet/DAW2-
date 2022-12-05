#!/usr/bin/python3
import sqlite3

conn = sqlite3.connect("./bd/BD1.sqlite")

cur = conn.cursor()

cur.execute('CREATE TABLE USUARIOS(NOMBRE VARCHAR(30), APELLIDOS VARCHAR(50), SEXO VARCHAR(8))')

conn.commit()
cur.close()
conn.close()

print("Content-Type: text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Creada BD</title>")
print("</head>")
print("<body>")
print("<h2>Se ha creado la base de datos con exito</h2>")
print("</body>")
print("</html>")
