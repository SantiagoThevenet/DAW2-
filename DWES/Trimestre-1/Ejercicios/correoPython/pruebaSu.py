from email.message import EmailMessage
import smtplib,ssl

port = 465
server = 'smtp.gmail.com'

sender = 'santiDAW1234@gmail.com'
reciver = 'santiDAW1234@gmail.com'

password = 'bkrdntaaggoeqfff'

subject = 'Combrueba la cabezera suuuuuuuuuuuu'
body = 'Tengo algo que contarte'

message = EmailMessage()

message['From'] = sender
message['To'] = reciver
message['Subject'] = subject

message.set_content(body)

contexto = ssl.create_default_context()

with smtplib.SMTP_SSL(server,port,context = contexto) as s:
    s.login(sender,password)
    s.sendmail(sender,reciver,message.as_string())


