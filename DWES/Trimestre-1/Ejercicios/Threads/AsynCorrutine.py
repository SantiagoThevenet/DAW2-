from datetime import datetime
from random import randint
from asyncio import coroutine, sleep, Task, get_event_loop



info = []
results = []

#Ahora las funcione sla defino como corrutinas con async
async def generate_info():
    while True:
        await sleep(1) #esta es la parte de esperar cuando queremos (pausa explicita)
        info.append("Something at {}".format(datetime.now()))
        print("New info added\n")

        
async def process_info():
    while True:
        await sleep(1)
        print("Cheking for new info\n")
        if info:
            new_info = info.pop()
            results.append(new_info + " processed")
            print("New info processed --> " + new_info, end="\n")

loop = get_event_loop()

generator = loop.create_task(generate_info())
processor1 = loop.create_task(process_info())
processor2 = loop.create_task(process_info())

loop.run_forever()

##generator.start()
##processor1.start()
##processor2.start()
##
##generator.join() #esperar a que acabe el generator y ya puedo terminar el hilo principal o main
