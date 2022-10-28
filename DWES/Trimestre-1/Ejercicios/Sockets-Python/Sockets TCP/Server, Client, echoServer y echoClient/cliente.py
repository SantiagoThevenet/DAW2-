import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c:
    c.connect((HOST, PORT))
    c.send("GET / HTTP 1.1 200 OK \r\n\r\n hola mundo".encode('utf-8'))
    data = c.recv(1024)

print('Received from Server:', data.decode('utf-8')) #decode retorna un string a partir de una representación de bytes.
