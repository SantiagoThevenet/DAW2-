import socket

HOST = 'localhost'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Waiting connections.......")
    conn, addr = s.accept() #conn es un nuevo socket para comunicar con el cliente
    
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print('Datos recibidos desde el Cliente: {}'.format(data.decode('utf-8')))
            conn.sendall(data)
