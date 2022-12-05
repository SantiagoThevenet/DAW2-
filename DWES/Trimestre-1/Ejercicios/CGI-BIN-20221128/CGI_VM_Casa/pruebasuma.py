#!/usr/bin/python3
import matematicas

a=6
b=4

print("Content-Type: text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hola mundo - Primer programa CGI</title>")
print("</head>")
print("<body>")
print("<h2>HOLA MUNDO! Mi primer programa CGI</h2>")
print(matematicas.suma(a,b))
print("</body>")
print("</html>")


