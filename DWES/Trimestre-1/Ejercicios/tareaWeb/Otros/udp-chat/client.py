import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as c:
    while True:    
        msg = '>'+input(">")
        c.sendto(msg.encode('utf-8'), ('localhost', 65432))
        data, addr = c.recvfrom(4096)
        print(data.decode('utf-8'))
