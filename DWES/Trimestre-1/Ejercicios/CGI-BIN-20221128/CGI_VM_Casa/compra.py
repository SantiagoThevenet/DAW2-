#!/usr/bin/python3

import cgi, mysql.connector

form = cgi.FieldStorage()
lista_prod = []
lista_cantidad = []
cont = 0

for i in form:
	if 'chk' in i:
		lista_prod.append(int(i.replace('chk_','')))
	
	# if 'txt' in i:
		# lista_cantidad.append(form.getvalue('txt_'+str(cont)))
		# cont =cont + 1

miConex = mysql.connector.connect(
	host='localhost',
	user='root',
	passwd='luis',
	database='GAMES')

miCursor = miConex.cursor(prepared=True)

for i in lista_prod:
	#miCursor.execute("SELECT NOMBRE, PRECIO FROM PRODUCTOS WHERE COD_PROD=?;",(i))


	miCursor.execute("UPDATE PRODUCTOS SET CANTIDAD = CANTIDAD-1 WHERE COD_PROD=?;",(i,))
	miConex.commit()
	
	
	
	
print("Content-Type: text/html\r\n\r\n")
print("<meta charset='UTF-8'>")
#print(lista_cantidad)

#miCursor.execute("SELECT NOMBRE, PRECIO FROM PRODUCTOS WHERE COD_PROD=1")

#l = miCursor.fetchone()
#for i in l:
#	print(i)
#for i in form:
	#print(i)


#print(lista_prod)

if lista_prod:
	print("<h2>Has comprado:</h2>")
	for i in lista_prod:
		miCursor.execute("SELECT NOMBRE, PRECIO, CATEGORIA FROM PRODUCTOS WHERE COD_PROD=?",(i,))

		l = miCursor.fetchone()
		print("<h3>Producto:", l[0] + ";\tPrecio:", l[1], "€;\tCategoria:" + l[2] + "</h3>")

	print("<h1><p>Gracias por su confianza</p></h1>")
	print("<h3><p>Se le ha enviado un correo con los detalles de su compra</p></h3>")
else:
	print("Tu carro esta vacío")
