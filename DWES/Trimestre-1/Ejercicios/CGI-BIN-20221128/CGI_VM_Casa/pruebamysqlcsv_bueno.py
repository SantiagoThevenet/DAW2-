#!/usr/bin/python3

# print("Creando bases de datos y rellenandolas!!!")
# import mysql.connector

# con = mysql.connector.connect(host="localhost", user="root", passwd="luis")

# if con.is_connected():
	# print("Conexión establecida!!!")
	
	# cur = con.cursor()
	# cur.execute("SHOW DATABASES;")
	# #print(cur)
	
	# for bd in cur:
		# print(bd)
		
	# cur.close()
	# con.close()
	




# if not con.is_connected():
	# print("Conexión finalizada!!!")



import mysql.connector, csv

try:

    miConex = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='luis')

    if miConex.is_connected():

        print("Conexión establecida correctamente!!!")

    miCursor = miConex.cursor()
    miCursor.execute("CREATE DATABASE GAMES;")
    miCursor.execute("USE GAMES;")

    miCursor.execute("CREATE TABLE PRODUCTOS(\
                    COD_PROD INT PRIMARY KEY AUTO_INCREMENT, NOMBRE VARCHAR(30)\
                    , CATEGORIA VARCHAR(30), PRECIO FLOAT, CANTIDAD INT)")

##    miCursor.execute("INSERT INTO PRODUCTOS VALUES(NULL,?,?,?,?)")
##    miConex.commit()

    miCursor = miConex.cursor(prepared=True)
    productos = []
    with open('productos.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for i in csv_reader:
            productos.append(tuple(i))
        


        miCursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL,?,?,?,?)",productos)
    
    
    miConex.commit()
    miConex.close()

    


except Exception as e:

    print("Error de conexión!!!")
    print(e)

    

print("Todo correcto!!!")
