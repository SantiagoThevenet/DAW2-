import socket
import socket
HOST = 'localhost'
PORT = 65432


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        print('Esperando peticiones...')
        conn, addr = s.accept()
        with conn:
            print(f"NOMBRE DEL HOST: {socket.gethostname()}\n")
            while True:
                data = conn.recv(1024)
                print(data.decode("utf-8"))
                messageS = '-'+input('-')
                if messageS == '-exit':
                    break
                conn.send(messageS.encode('utf-8'))
