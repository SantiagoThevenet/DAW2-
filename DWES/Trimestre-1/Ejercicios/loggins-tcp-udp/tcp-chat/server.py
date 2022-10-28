import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('localhost', 65432))
    s.listen(5)
    while True:
        print('Esperando peticiones...')
        conn, addr = s.accept()
        with conn:
            while True:
                print(conn.recv(1024).decode('utf-8'))
                message = '-'+input('-')
                conn.sendall(message.encode('utf-8'))
