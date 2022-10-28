import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c:
    c.connect(('127.0.0.1',65432))
    c.sendall(b'hehehe suuuuuuuu')

    print(repr(c.recv(2048)))