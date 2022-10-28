import socket

serv_sock = socket.socket(
    socket.AF_INET,  # set internet protocol(IP)
    socket.SOCK_STREAM,  # set socket type to 'stream' (TCP)
    proto=0  # set the default protocol (for TCP it's IP)
)
serv_sock.bind(('127.0.0.1', 6543))

serv_sock.listen(1)
while True:
    client_sock, client_addr = serv_sock.accept()
    print('New connection from', client_addr)
    chunks = []
    while True:
        data = client_sock.recv(2048)
        if not data:
            break
        chunks.append(data)
    client_sock.sendall(b''.join(chunks))
    client_sock.close()
