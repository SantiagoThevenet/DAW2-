import csv
import yagmail
import random
receiver = "santiDAW1234@gmail.com"

with open('./correos.csv') as file:
    reader = csv.reader(file)
    next(reader) 
    for nombre,comentario,documento,documento2 in reader:
        yag = yagmail.SMTP("santiDAW1234@gmail.com")
        numRan = random.randrange(0,2)
        if numRan == 0:
            documento = [documento,documento2] 
            
        print(numRan)
        yag.send(
            to=receiver,
            subject=f"Esto es para ti {nombre}",
            contents=comentario, 
            attachments=documento
        )
        print(f"Enviado con exito a {nombre}")
        documento = ''
