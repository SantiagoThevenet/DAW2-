#!/usr/bin/python3

import cgi, os
import cgitb

cgitb.enable()

form = cgi.FieldStorage()

# Get filename here.
fileitem = form['filename']

# Test if the file was uploaded
if fileitem.filename:
   
   # strip leading path from file name to avoid 
   # directory traversal attacks
   fn = os.path.basename(fileitem.filename)
   #open('/tmp/' + fn, 'wb').write(fileitem.file.read())   
   #fn = os.path.basename(fileitem.filename.replace("\\", "/" ))
   with open("/tmp/"+fn, "wb") as writer:
	   
	   writer.write(fileitem.file.read())
   

   message = 'The file "' + fn + '" was uploaded successfully'
   
else:
   message = 'No file was uploaded'

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Upload File- Eigth CGI Program</title>")
print("</head>")
print("<body>")
print("<p>%s</p>" % message)
print("</body>")
print("</html>")
