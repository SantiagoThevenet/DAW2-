import socket
client_sock = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

client_sock.connect(('127.0.0.1', 6543))
client_sock.sendall(b'Hello world')

# client_sock.shutdown(socket.SHUT_WR) #A terminado el envio

chunks = []
while True:
    data = client_sock.recv(2048)
    if not data:
        break
    chunks.append(data)
# print('Received', repr(b''.join(chunks)))
print('Received',b''.join(chunks).decode())

client_sock.close()
