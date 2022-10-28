import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c:
    c.connect(('localhost', 65432))
    while True:
        message = '>'+input('>')
        c.sendall(message.encode('utf-8'))
        print(c.recv(1024).decode('utf-8'))
