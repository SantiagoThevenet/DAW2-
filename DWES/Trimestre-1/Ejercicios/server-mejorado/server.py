import socket 

HOST = 'localhost'
PORT = 65432


with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()

    while True:
        print('Print esperando peticiones...')
        conn,addr = s.accept()
        with conn:
            print('Conectado con: ', addr)
            conn.send('Hola, bienvenido a mi servidor'.encode('utf-8'))
            while True:
                data = conn.recv(1024)
                if not data:
                    break

                print(f'Datos recibidos desde el Cilente {data.decode("utf-8")}')