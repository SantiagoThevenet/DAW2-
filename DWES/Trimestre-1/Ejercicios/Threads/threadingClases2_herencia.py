import threading
import time

class Hello(threading.Thread):

    def run(self):
        for i in range(5):
            print("Hello")
            time.sleep(1)


class Goodbye(threading.Thread):
    def run(self):
        for i in range(5):
            print("GoodBye")
            time.sleep(1)

            

t1 = Hello()
t2 = Goodbye()

t1.start()
t2.start()

##t1.join()
##t2.join()
##
##print("SE ACABO")
