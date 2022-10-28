import threading

def holamundo():
    print("Hola mundo")

if __name__ == '__main__':

    hilo = threading.Thread(target=holamundo) #Coódigo a ejecutar en segundo plano
    hilo.start()
#    hilo.joion()
