#!/usr/bin/python3

# Import modules for CGI handling 
from os import environ
import cgi, cgitb

cgitb.enable()

if 'HTTP_COOKIE' in environ:
	
   print(environ)
   for cookie in map(strip, split(environ['HTTP_COOKIE'], ';')):
      (key, value ) = split(cookie, '=');
      if key == "UserID":
         user_id = value

      if key == "Password":
         password = value

print("User ID  = %s" % user_id)
print("Password = %s" % password)
