import socket
HOST = 'localhost'
PORT = 65400
buffersize = 4096

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST,PORT))

    while True:
        print("Escuchando peticiones desde", s.getsockname())
        data, addr = s.recvfrom(buffersize)
        print("Mensaje del Cliente:", data.decode('utf-8'))
        # s.sendto(data, addr)
