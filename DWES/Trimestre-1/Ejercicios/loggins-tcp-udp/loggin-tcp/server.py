import socket
import logging

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('localhost', 65432))
    s.listen(5)
    conn, addr = s.accept()
    logging.basicConfig(filename='log.log',filemode='w',format=f'{addr} - %(message)s - %(asctime)s', datefmt='%d-%b-%y %H:%M:%S')
    try:
        while True:
            print('Esperando peticiones...')
            with conn:
                while True:
                    print(1/0)
                    print(conn.recv(1024).decode('utf-8'))
                    message = '-'+input('-')
                    conn.sendall(message.encode('utf-8'))
    except Exception as e:
        logging.exception(e)
