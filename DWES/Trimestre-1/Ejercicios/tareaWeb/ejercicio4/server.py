import socket,yagmail

PORT = 65431
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind(('localhost',PORT))
    s.listen()
    cont = 0
    while True:
        conn, addr = s.accept()
        listaCliente = conn.recv(2048)
        print(listaCliente.decode('utf-8'))
        