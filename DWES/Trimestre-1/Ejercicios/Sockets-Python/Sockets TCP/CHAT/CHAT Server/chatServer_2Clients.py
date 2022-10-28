import socket

HOST = 'localhost'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Server Info:", socket.gethostname(), "Port:", PORT, "IP:", socket.getaddrinfo(HOST, PORT)[1][4][0])
    print("Waiting 2 connections...")
##    print("BIENVENIDO AL SERVIDOR DE CHAT POR SOCKETS!!!")
##    print("SE BUENO Y NO SERÁS BANEADO. DISFRUTA!!!")
    
    conn, addr = s.accept() #conn es un nuevo socket para comunicar con el cliente
    print('Connected by client 1', addr)
    print("Waiting 1 connection...")
    conn2, addr2 = s.accept() #conn es un nuevo socket para comunicar con el cliente
    print('Connected by client 2', addr)

    
    with conn as c1, conn2 as c2:
        print('Connected by client 1', addr)
        c1.send('Bienvenido al servidor de Chat'.encode('utf-8'))
        print('Connected by client 2', addr)
        c2.send('Bienvenido al servidor de Chat'.encode('utf-8'))
        
        while True:

            send = input("Server->")
            c1.send(send.encode('utf-8'))
            c2.send(send.encode('utf-8'))
            print("Message sent...")

            data = c1.recv(1024)            
            data2 = c2.recv(1024)
            
            print("Cliente1--", data.decode('utf-8'))
            c1.send(data2)
            print("Cliente2--", data.decode('utf-8'))
            c2.send(data)

##            if data.decode('utf-8') == 'exit':
##
##                break



