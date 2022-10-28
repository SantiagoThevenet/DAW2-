import time
from datetime import datetime
from random import randint
from threading import Thread


info = []
results = []

def generate_info():
    while True:
        time.sleep(1)
        info.append("Something at {}".format(datetime.now()))
        print("New info added\n")

        
def process_info():
    while True:
        time.sleep(1)
        print("Cheking for new info\n")
        if info:
            new_info = info.pop()
            results.append(new_info + " processed")
            print("New info processed --> " + new_info, end="\n")

generator = Thread(target=generate_info) #hilo 1
processor1 = Thread(target=process_info) #hilo 2
processor2 = Thread(target=process_info) #hilo 3

generator.start()
processor1.start()
processor2.start()

generator.join() #esperar a que acabe el generator y ya puedo terminar el hilo principal o main
