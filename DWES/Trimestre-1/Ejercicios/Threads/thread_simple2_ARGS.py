import threading,time

def holamundo(nombre):
    print("Hola mundo " + nombre)
    #time.sleep(5)

if __name__ == '__main__':

    hilo = threading.Thread(target=holamundo, args=("LUIS",)) #Coódigo a ejecutar en segundo plano
    hilo.start()

##    print("Hola mundo perranganos!!!")
#Solución ENTER cuando hay hilos de por medio que no se quede pillado y flushee el buffer
##print("\n")

##Solucion buena para que no pase eso es un join para el thread
##    hilo.join()
