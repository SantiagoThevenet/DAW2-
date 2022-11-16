import socket

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as c:
    c.connect(('localhost',65432))
    
    while True:
        messageC2 = c.recv(2048).decode('utf-8')
        print(messageC2)
        
        messageC1 = input('}').encode('utf-8')
        c.sendall(messageC1)    
        
        messageS = c.recv(2048).decode('utf-8')
        print('>'+messageS)
        
        