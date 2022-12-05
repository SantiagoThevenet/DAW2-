import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c:
    c.connect(('localhost', 65431))
    print(f"Chateadno con: {socket.gethostname()}\n")

    while True:
        messageC = '>'+input('>')
        if messageC == '>exit':
            break
        c.send(messageC.encode('utf-8'))
        data = c.recv(1024)
        print(data.decode('utf-8'))