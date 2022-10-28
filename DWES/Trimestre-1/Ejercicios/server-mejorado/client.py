import socket

HOST = 'localhost'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c:
    c.connect((HOST,PORT))
    # print(f"NOMBRE DEL HOST: {socket.gethostname()}")
    # c.connect('mensaje'.encode('utf-8'))
    # c.sendall(bytes('Soy el puto amo', encoding='utf-8'))
    c.send("Hola desed el cliente".encode('utf-8'))
    # data = c.recv(8)


    a = True
    while a:
        data = c.recv(8)
        print(data.decode('utf-8'))
        if not data:
            a = False

print(f"Recived form Server: {data.decode('utf-8')}")
