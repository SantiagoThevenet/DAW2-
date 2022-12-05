#!/usr/bin/python3

#Source file name : download.py
#HTTP Header
fileName='downloadedFile'
print("Content-Type:application/octet-stream; name=\"%s\"\r\n" %fileName)
print("Content-Disposition: attachment; filename=\"%s\"\r\n\r\n" %fileName)

data= ''

try:
    with open('/tmp/ficherosubido.txt','rb') as fo: 
        data = fo.read();
    print(data )
except Exception as e:
    print("Content-type:text/html\r\n\r\n")
    print('<br>Exception :')
    print(e)
