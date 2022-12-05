#!/usr/bin/python3
# -*- coding: UTF-8 -*-
#

import cgi
from http import cookies


miCookie = cookies.SimpleCookie()
miCookie["pref_lang"] = "es"
miCookie["pref_lang"]["expires"] = "Wed, 28 Aug 2022 18:30:00 GMT"
miCookie["pref_lang"]["domain"] = "localhost"

print(miCookie.output())

print("Content-Type: text/html\r\n\r\n")
print("""
<html>
	<head>
		<meta charset="utf-8">
		<title>CGI-Cookie</title>
	</head>
    <body>
        <h1>Cookie set OK!</h1>
    </body>
</html>
""")
#print(miCookie.output())



