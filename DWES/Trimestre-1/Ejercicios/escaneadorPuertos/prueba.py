import threading
import socket
import time

nThreads = 4
lista = []

def worker2(rango_ini, rango_fin):
    for i in range(rango_ini, rango_fin):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            puerto = s.connect_ex(('127.0.0.1', i))
            if puerto == 0:
                lista.append(i)
                
    return lista


porst = 65535//nThreads
listPorts = []
t0 = time.time()

threads = []

for i in range(nThreads):
    listPorts.append(porst*i)
    t = threading.Thread(target=worker2, args=(listPorts[i], porst*(i+1),))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

tf = time.time() - t0


print(lista)
print("\nTiempo total con {} thread {}\n".format(nThreads, tf))
