import threading
import time
import socket


'''VERSION CON HILOS '''

n_threads = 2
lista2 = list()


def worker2(rango_ini, rango_fin):
    for i in range(rango_ini, rango_fin):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            puerto = s.connect_ex(('127.0.0.1', i))
            if puerto == 0:
                lista2.append(i)
                
    return lista2


p = 65535//n_threads
inicios = list()
fines = list()

inicio = 0
fin = p

for i in range(n_threads):
    inicios.append(inicio)
    fines.append(fin)
    inicio += p
    fin += p

t0 = time.time()
threads = list()
for i in range(len(inicios)):
    t = threading.Thread(target=worker2, args=(inicios[i], fines[i],))
    threads.append(t)
    t.start()


for t in threads:
    t.join()

tf = time.time() - t0


print(lista2)
print("\nTiempo total con {} thread {}\n".format(n_threads, tf))
lista2.sort()
