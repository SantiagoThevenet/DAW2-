import socket

HOST = 'localhost'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c2:
    c2.connect((HOST, PORT))
    print(f"NOMBRE DEL HOST: {socket.gethostname()}\n")

    while True:
        messageC = '='+input('=')
        if messageC == '=exit':
            break
        c2.send(messageC.encode('utf-8'))
        data = c2.recv(1024)
        print(data.decode('utf-8'))