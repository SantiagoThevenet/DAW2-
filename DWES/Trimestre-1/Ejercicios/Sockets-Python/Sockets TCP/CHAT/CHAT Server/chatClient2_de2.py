import socket

HOST = 'localhost'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c:
    
    c.connect((HOST, PORT))

    respuesta = c.recv(1024)
    print(respuesta.decode('utf-8'))

    while True:
        
        respuesta = c.recv(1024)
        print("Server->", respuesta.decode('utf-8'))
        msg = input("--")
        c.send(msg.encode('utf-8'))
        
##        if msg == 'exit':
##
##            break

        

print("ADIOS")
    
   
