#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 

from http import cookies
# C = cookies.SimpleCookie()
# C["fig"] = "newton"
# C["sugar"] = "wafer"
# print(C)

C = cookies.SimpleCookie()
C["oreo"] = "querica"
C["oreo"]["expires"] = "Wed, 28 Aug 2022 18:30:00 GMT"
C["oreo"]["domain"] = "localhost"



print(C)

#print('Set-Cookie: name="prueba"; expires=Wed, 28 Aug 2022 18:30:00 GMT; UserID = "LUIS"; Password = "LUIS1234"')
#print('Set-Cookie: name="prueba"\r\n\r\n')
#print('Set-Cookie: UserID = "LUIS"\r\n')
#print('Set.Cookie: Password = "LUIS1234"\r\n\r\n')

#print("Set-Cookie: UserID = LUIS;\r\n")
#print("Set-Cookie: Password = LUIS1234\r\n")
#print('')
print("""
<html>
	<head>
		<meta charset="utf-8">
		<title>w3big.com</title>
	</head>
    <body>
        <h1>Cookie set OK!</h1>
    </body>
</html>
""")
