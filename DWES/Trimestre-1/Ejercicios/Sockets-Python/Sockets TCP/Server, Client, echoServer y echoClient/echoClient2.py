import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

mensaje = "Hola mundo!!!"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(mensaje.encode('utf-8')) #encode retorna una representación de bytes del string dado.
    #s.sendall(bytes("Soy el puto amo", encoding='utf-8'))
    data = s.recv(1024)

print('Received from Server:', repr(data.decode('utf-8'))) #decode retorna un string a partir de una representación de bytes.
