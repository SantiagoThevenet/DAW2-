import socket,csv

PORT = 65431
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as c:
    c.connect(('localhost',PORT))
    
    with open('./clientes.csv') as file:
        clienteCSV = csv.reader(file)
        next(clienteCSV)
        for nombre,correo,gustos in clienteCSV:
            messagec = [nombre,correo,gustos]
            c.sendall(messagec)
