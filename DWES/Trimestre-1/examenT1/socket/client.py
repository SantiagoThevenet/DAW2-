import socket

# # CLIENTE TCP

# with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as c:
#     c.connect(('localhost',65431))
#     while True: 
#         messageC = str('-'+input('-'))
#         c.send(messageC.encode('utf-8'))
        
#         data = c.recv(1024)
#         print(data.decode('utf-8'))






# # CLIENTE UDP
# with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as c:
#     msg = input(">")
#     c.sendto(msg.encode('utf-8'),('localhost',65400))
#     data, addr = c.recvfrom(4096)
#     print("-", data.decode('utf-8'))


with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as c:
    c.connect(('localhost',65432))
    
    while True:
        messageC1 = input('-').encode('utf-8')
        c.sendall(messageC1)    
        
        messageC2 = c.recv(2048).decode('utf-8')
        print(messageC2)
        
        messageS = c.recv(2048).decode('utf-8')
        print('>'+messageS)
