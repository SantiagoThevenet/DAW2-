#!/usr/bin/python3
import cgi,cgitb,mysql.connector,csv

form = cgi.FieldStorage()

miDatabase = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "Santi1234"
	)


if miDatabase.is_connected():
	print('Tienes un 10 facil')




cursor = miDatabase.cursor()

nombre = form.getvalue('nombre')
email = form.getvalue('email')
genero = form.getvalue('genero')
password = form.getvalue('password')
tipo = form.getvalue('tipo')


cursor.execute("USE USERS;")		
cursor.execute(f"INSERT INTO usuarios value('{nombre}','{email}','{genero}','{password}','{tipo}')")
miDatabase.commit()
