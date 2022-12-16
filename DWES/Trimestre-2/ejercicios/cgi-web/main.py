import mysql.connector,csv

miConex = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'santi'
)

miCursor = miConex.cursor()


miCursor.execute('USE MENU;')
miCursor.execute('')