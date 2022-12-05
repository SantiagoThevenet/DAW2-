#!/usr/bin/python3

# HTTP Header
print("Content-Type:application/octet-stream;\r\n")
print("Content-Disposition: attachment; filename = 'ficherobajado.txt'\r\n\r\n")
print("<html>Guardame</html>")

# Actual File Content will go here.
fo = open("/tmp/ficherosubido.txt", "rb")

contenido = fo.read();
print(contenido)

# Close opend file
fo.close()
