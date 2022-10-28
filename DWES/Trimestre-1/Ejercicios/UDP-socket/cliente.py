import socket
HOST = 'localhost'
PORT = 65400
buffersize = 4096

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as c:
    msg = input(">")
    c.sendto(msg.encode('utf-8'),(HOST,PORT))
    # data, addr = c.recvfrom(4096)
    # print("Mensaje del Servidor ECHO:", data.decode('utf-8'))
