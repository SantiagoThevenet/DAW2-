import smtplib, ssl
import getpass
port = 465

# password = getpass.getpass('Password:')
password = 'bkrdntaaggoeqfff'
sender_mail = "santiDAW1234@gmail.com"
receiver_mail = "daw2122mrt@gmail.com"
server_domain = "smtp.gmail.com"
msg = '''Subject: Hola mundo
Este es un mensaje de prueba'''
context = ssl.create_default_context()

with smtplib.SMTP_SSL(server_domain, port, context=context) as s:
    s.login(sender_mail, password)
    s.sendmail(sender_mail, receiver_mail, msg)
    
print("Email enviado!!!")
