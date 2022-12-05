import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('localhost', 65431))
    s.listen()
    while True:
        print('Esperando peticiones...')
        conn, addr = s.accept()
        with conn:
            print(f"Chateadno con: {socket.gethostname()}\n")
            while True:
                data = conn.recv(2048)
                print(data.decode("utf-8"))
                messageS = '-'+input('-')
                if messageS == '-exit':
                    break
                conn.send(messageS.encode('utf-8'))
