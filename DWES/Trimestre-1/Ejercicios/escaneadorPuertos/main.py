import socket
import time
import threading

ip = '127.0.0.1'
n_threads = 2

def escanearPuerto(rango1, rango2):
    for i in range(rango1, rango2):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            puerto = s.connect_ex((ip, i))
            if puerto == 0:
                print(f"Puerto: {i} abierto")


p = 65535//n_threads
inicios = list()
fines = list()

inicio = 0
fin = p
threads = []

if __name__ == '__main__':
    timpoInicio = time.time()

    for i in range(n_threads):
        inicios.append(inicio)
        fines.append(fin)
        inicio += p
        fin += p
    

    for i in range(n_threads):
        t = threading.Thread(target=escanearPuerto, args=(inicios[i], fines[i],))
        threads.append(t)
        t.start()
    
    for i in threads:
        i.join()

    print(f"Tiempo total: {time.time() - timpoInicio}")
