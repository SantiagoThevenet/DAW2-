import socket

HOST = 'localhost'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c:
    
    c.connect((HOST, PORT))
    msg_inicio = c.recv(1024)
    print(msg_inicio.decode('utf-8'))

    while True:

        msg = input("--")
        c.send(msg.encode('utf-8'))
        request = c.recv(1024)


        print("->", request.decode('utf-8'))

print("ADIOS")
    
   
