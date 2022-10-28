import socket
import logging

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('localhost', 65431))
    s.listen(5)
    
    while True:
        print('Esperando peticiones...')
        conn1, addr = s.accept()
        try: 
            with conn1:
                while True:
                    print('Esperando peticiones...')
                    conn2, addr2 = s.accept()
                    logging.basicConfig(filename='log.log',filemode='w',format=f'{addr2} - %(message)s - %(asctime)s', datefmt='%d-%b-%y %H:%M:%S')
                    try:
                        with conn2:
                            while True:
                                messageC1 = conn1.recv(1024).decode('utf-8')
                                conn2.sendall(messageC1.encode('utf-8'))
                                print (messageC1)
                                messageC2 = conn2.recv(1024).decode('utf-8')
                                conn1.sendall(messageC2.encode('utf-8'))
                                print(messageC2)

                                message = '-'+input('-')

                                conn1.sendall(message.encode('utf-8'))
                                conn2.sendall(message.encode('utf-8'))
                    except Exception as e:
                        logging.exception(e)
        except Exception as e:
            logging.exception(e)
