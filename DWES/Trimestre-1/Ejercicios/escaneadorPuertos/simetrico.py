import socket
import time

timpoInicio = time.time()
for i in range(65535):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        puerto = s.connect_ex(('127.0.0.1', i))
    
        if puerto == 0:
            print(f'Puerto {i} abierto')

