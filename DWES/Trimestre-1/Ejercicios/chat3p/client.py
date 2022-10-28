import socket

HOST = 'localhost'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c1:
    c1.connect((HOST, PORT))
    print(f"NOMBRE DEL HOST: {socket.gethostname()}\n")

    while True:
        messageC = '>'+input('>')
        if messageC == '>exit':
            break
        c1.send(messageC.encode('utf-8'))
        data = c1.recv(1024)
        print(data.decode('utf-8'))