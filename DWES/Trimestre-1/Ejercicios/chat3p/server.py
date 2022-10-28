from cmath import log
import socket
HOST = 'localhost'
PORT = 65432


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        print('Esperando peticiones...')
        conn, addr = s.accept()
        clientes = []
        print(cli)
        if addr not in clientes:
            clientes.append(addr)
        while len(clientes) == 2:
            data = conn.recv(1024)
            print(data.decode("utf-8"))
            messageS = '-'+input('-')
            if messageS == '-exit':
                break
            conn.send(messageS.encode('utf-8'))
