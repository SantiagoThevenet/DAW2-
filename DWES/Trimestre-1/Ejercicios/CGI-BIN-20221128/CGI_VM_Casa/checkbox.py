#!/usr/bin/python3

#Import modules for CGI handling 
import cgi, cgitb 

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
if form.getvalue('maths'):
   math_flag = "ON"
else:
   math_flag = "OFF"

if form.getvalue('pyshics'):
   physics_flag = "ON"
else:
   physics_flag = "OFF"

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Checkbox - Third CGI Program</title>")
print("</head>")
print("<body>")
print("<h2> CheckBox Maths is : %s</h2>" % math_flag)
print("<h2> CheckBox Physics is : %s</h2>" % physics_flag)
for i in lista:
	print("<h2>{}</h2>".format(i))
print("</body>")
print("</html>")
