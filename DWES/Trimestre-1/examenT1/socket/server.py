import socket

# #SERVIDOR TCP

# with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
#     s.bind(('localhost',65431))
# #     s.listen()
    
#     while True:
#         conn, addr = s.accept()
#         with conn:
#             while True:
#                 messageC = conn.recv(2048).decode('utf-8')
#                 print(messageC)
                
#                 messageS = str('>'+input('>'))
#                 conn.sendall(messageS.encode('utf-8'))


# #SERVIDOR UDP
# with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
#     s.bind(('localhost',65400))
    # while True:
#         data, addr = s.recvfrom(4096)
#         print(">", data.decode('utf-8')) 
#         s.sendto(data, addr)



with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind(('localhost',65432))
    s.listen()
    
    while True:
        sock, addr= s.accept()
        with sock:
            while True: 
                sock2, addr= s.accept()
                with sock2:
                    while True:
                        messageC1 = sock.recv(2048).decode('utf-8')      
                        sock2.sendall(messageC1.encode('utf-8'))
                        print('-'+messageC1)
                        messageC2 = sock2.recv(2048).decode('utf-8') 
                        sock.sendall(messageC2.encode('utf-8'))                             
                        print('}'+messageC2)
                        
                        messageS = input('>').encode('utf-8')
                        sock.sendall(messageS)
                        sock2.sendall(messageS)