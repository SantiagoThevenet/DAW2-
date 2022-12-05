#!/usr/bin/python3
# -*- coding: UTF-8 -*-
#

import cgi, os
from http import cookies


# miCookie = cookies.SimpleCookie()
# miCookie["pref_lang"] = "es"
# miCookie["pref_lang"]["expires"] = "Wed, 28 Aug 2022 18:30:00 GMT"
# miCookie["pref_lang"]["domain"] = "localhost"

# print(miCookie.output())


def show_cookie(c):
	
	#print(c.)
	for key, morsel in c.items():
		
		print("key = ", morsel.key)
		print("<br>")
		print("value = ", morsel.value)
		print("<br>")
		print("coded_value = ", morsel.coded_value)
		print("<br>")
		
		for name in morsel.keys():
			if morsel[name]:
				print("{}: {}".format(name, morsel[name]))
	return ''

print("Content-Type: text/html\r\n\r\n")
print("""
<html>
	<head>
		<meta charset="utf-8">
		<title>CGI-Cookie Recovery</title>
	</head>
    <body>
        <h1>Cookie Recovery Data: OK!</h1>
    </body>
</html>
""")
# if "HTTP_COOKIE" in os.environ:
	# print(os.environ["HTTP_COOKIE"])
# else:
	# print("Not exists Cookie")
	
# user_lang = cookies.SimpleCookie(os.environ["HTTP_COOKIE"])
# print(user_lang["pref_lang"].value)
	
try:
	
	user_lang = cookies.SimpleCookie(os.environ["HTTP_COOKIE"])
	print("Lenguaje preferido para usar:",user_lang["pref_lang"].value)
	print("<br>")
	#print("Fecha de expiración:",user_lang["pref_lang"]["expires"].value)
	#print("Dominio de la Cookie:",user_lang["pref_lang"]["domain"].value)
	print(show_cookie(user_lang))
	
except(cookies.CookieError, KeyError):
	
	print("Not exists a valid Cookie!!!")
	
