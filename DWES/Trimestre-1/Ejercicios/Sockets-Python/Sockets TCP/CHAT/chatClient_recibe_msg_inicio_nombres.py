import socket

HOST = 'localhost'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

prompt_defecto = "--"


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c:
    
    c.connect((HOST, PORT))
    msg_inicio = c.recv(1024)
    print(msg_inicio.decode('utf-8'))

    name = input("Introduce un nombre de usuario: ")

    while True:

        if name == '':
            
            msg = input(prompt_defecto)
            
        else:
            
            msg = input(name + ">")
            


        msg = name + ">" + msg
        c.send(msg.encode('utf-8'))
        request = c.recv(1024)


        print(request.decode('utf-8'))

print("ADIOS")
    
   
