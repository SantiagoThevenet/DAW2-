import time
from datetime import datetime
from random import randint
from multiprocessing import Process, Manager

shared_memory = Manager() #para compartir memoria

info = shared_memory.list([]) #lista compartida en memoria
results = shared_memory.list([])#lista compartida en memoria

def generate_info(info):
    while True:
        time.sleep(1)
        info.append("Something at {}".format(datetime.now()))
        print("New info added\n")

        
def process_info(info, results):
    while True:
        time.sleep(1)
        print("Cheking for new info\n")
        if info:
            new_info = info.pop()
            results.append(new_info + " processed")
            print("New info processed --> " + new_info, end="\n")

generator = Process(target=generate_info, args=[info]) #proceso 1
processor1 = Process(target=process_info, args=[info, results]) #proceso 2
processor2 = Process(target=process_info, args=[info, results]) #proceso 3

generator.start()
processor1.start()
processor2.start()

generator.join() #esperar a que acabe el generator y ya puedo terminar el hilo principal o main
