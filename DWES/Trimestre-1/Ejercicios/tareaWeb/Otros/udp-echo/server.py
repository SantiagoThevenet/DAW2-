import socket

with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as s:
    s.bind(('localhost',65432))
    while True:
        print("Escuchando peticiones desde", s.getsockname())
        data, addr = s.recvfrom(4096)
        print("Mensaje del Cliente:", data.decode('utf-8'))
        s.sendto(data, addr)
