import threading
import time


def worker():

    
    print('Inicio')
    time.sleep(2)
    print('Fin')

##worker()


threads = list()
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

for t in threads:

    t.join() ##Hace que esperen a que acaben los hilos activados arriba

    
