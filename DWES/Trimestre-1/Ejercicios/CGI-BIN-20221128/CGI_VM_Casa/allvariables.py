#!/usr/bin/python3
import os
print("Content-Type: text/html\r\n\r\n")
print("<font-size=+1>Envirorement</font></br>")

for param in os.environ.keys():
	print("<b>%s</b>: %s</br>" % (param, os.environ[param]))
	#print(param)


print(os.environ["HTTP_COOKIE"])
#print(os.environ["HTTP_COOKIE"].keys())
