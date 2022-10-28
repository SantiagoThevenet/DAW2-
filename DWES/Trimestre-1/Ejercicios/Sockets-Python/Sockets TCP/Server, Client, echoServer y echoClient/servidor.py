import socket



HOST = 'localhost'  # Standard loopback interface address (localhost)
PORT = 65431      # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    while True:
        print("Esperando peticiones....")
        conn, addr = s.accept()

        with conn:
            print("Conectado con: ", addr)

            conn.send(f"HTTP/1.1 200 OK \r\n\r\n hola".encode())
        
