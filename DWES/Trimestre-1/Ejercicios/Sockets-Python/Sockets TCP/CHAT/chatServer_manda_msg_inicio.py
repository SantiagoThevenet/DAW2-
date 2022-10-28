import socket

HOST = 'localhost'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    msg_welcome = ("Server Name Info: {} Port: {} IP: {}\nBIENVENIDO AL SERVIDOR DE CHAT POR SOCKETS!!!\nSE BUENO Y NO SERÁS BANEADO. DISFRUTA!!!"
                   .format(socket.gethostname(),PORT, socket.getaddrinfo(HOST, PORT)[1][4][0]))\
                  
    
    s.bind((HOST, PORT))
    s.listen()
##    print("Server Info:", socket.gethostname(), "Port:", PORT, "IP:", socket.getaddrinfo(HOST, PORT)[1][4][0])
##    print("BIENVENIDO AL SERVIDOR DE CHAT POR SOCKETS!!!")
##    print("SE BUENO Y NO SERÁS BANEADO. DISFRUTA!!!")
    
    conn, addr = s.accept() #conn es un nuevo socket para comunicar con el cliente

    
    with conn:
        print('Connected by', addr)

        conn.send(msg_welcome.encode('utf-8'))
        
        while True:
            data = conn.recv(1024)

            print("--", data.decode('utf-8'))
            send = input("->")
            conn.send(send.encode('utf-8'))









            
##            if not data:
##                break
##            print('Datos recibidos desde el Cliente: {}'.format(data.decode('utf-8')))
##            conn.sendall(data)
