import socket
import threading
import time


def portScanner(rang1,rang2):
    for port in range(rang1,rang2):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as scanner:
            scanRes = scanner.connect_ex(('localhost',port))
            
            if scanRes == 0:
                print(f'Port: {port} aviable')  
                
numThreads = 2
portsRange  = 65535//numThreads

print(portsRange)
portScanner(portsRange)