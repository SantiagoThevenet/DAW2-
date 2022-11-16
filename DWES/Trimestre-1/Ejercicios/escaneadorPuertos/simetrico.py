import socket
import time


t0 = time.time()
for i in range(65535):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        puerto = s.connect_ex(('127.0.0.1', i))
    
        if puerto == 0:
            print(f'Puerto {i} abierto')
            
tf = time.time() - t0


print("\nTiempo total con {}\n".format(tf))
