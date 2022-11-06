from email.message import EmailMessage
import ssl,smtplib

host = 'smtp.gmail.com'
port = 465

sender = 'santiDAW1234@gmail.com'
reciver = 'santiDAW1234@gmail.com'
subject = 'Subject123123123'

password = 'bkrdntaaggoeqfff'

body='Young black art collector'

message = EmailMessage()

message['From'] = sender
message['To'] = reciver
message['Subject'] = subject


message.set_content(body)

contexto = ssl.create_default_context()

with smtplib.SMTP_SSL(host,port,context=contexto) as s:
    s.login(sender,password)
    s.sendmail(sender,reciver,message.as_string())


