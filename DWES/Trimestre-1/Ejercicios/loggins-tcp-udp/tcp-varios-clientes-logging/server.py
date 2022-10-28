import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('localhost', 65432))
    s.listen(5)
    while True:
        print('Esperando peticiones...')
        conn1, addr = s.accept()
        with conn1:
            while True:
                print('Esperando peticiones...')
                conn2, addr2 = s.accept()
                with conn2:
                    while True:
                        messageC1 = conn1.recv(1024).decode('utf-8')
                        conn2.sendall(messageC1.encode('utf-8'))
                        print (messageC1)
                        messageC2 = conn2.recv(1024).decode('utf-8')
                        conn1.sendall(messageC2.encode('utf-8'))
                        print(messageC2)

                        message = '-'+input('-')

                        conn1.sendall(message.encode('utf-8'))
                        conn2.sendall(message.encode('utf-8'))
        