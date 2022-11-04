import smtplib, ssl
import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
port = 465
password = 'bkrdntaaggoeqfff'
sender_mail = "santiDAW1234@gmail.com"
receiver_mail = ["santiDAW1234@gmail.com","federicodaw@gmail.com","daw2122mrt@gmail.com"]
server_domain = "smtp.gmail.com"
message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["From"] = sender_mail
message["To"] = receiver_mail
text = '''\
Hola
Como estas??
Espero que todo bien.
Luis
www.google.com
'''
html = '''\
<html>
<body>
<h1>Hola, <br>como estas??<br><b>espero que bien</b>
<a href="http://www.google.com">Enlace</a>
</h1>
</body>
</html>
'''
parte1 = MIMEText(text, "plain")
parte2 = MIMEText(html, "html")
message.attach(parte1)
message.attach(parte2)
context = ssl.create_default_context()
with smtplib.SMTP_SSL(server_domain, port, context=context) as s:
    s.login(sender_mail, password)
    s.sendmail(sender_mail, receiver_mail, message.as_string())
print("Email enviado!!!")