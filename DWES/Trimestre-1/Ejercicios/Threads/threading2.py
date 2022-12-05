import threading
import time


''' VERSION SINCRONA SIN HILOS '''


def worker1(rango):
    lista = list()
    for i in range(rango):
        lista.append(i)

    return lista


# t0 = time.time()

lista = worker1(100)

# tf = time.time() - t0

# print("Tiempo total en el thread {}\n".format(tf))
# print(lista)

'''VERSION CON HILOS '''

n_threads = 12
lista2 = list()


def worker2(rango_ini, rango_fin):
    for i in range(rango_ini, rango_fin):
        lista2.append(i)

    return lista2


p = len(lista)//n_threads
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
# print("\nLista ordenada")
# print(lista2)
