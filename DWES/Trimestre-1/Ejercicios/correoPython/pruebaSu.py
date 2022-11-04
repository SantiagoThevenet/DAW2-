from email.message import EmailMessage
import ssl, smtplib

sender = "santiDAW1234@gmail.com"
receiver = ["santiDAW1234@gmail.com","federicodaw@gmail.com","daw2122mrt@gmail.com"]
server = "smtp.gmail.com"
port = 465
password = 'bkrdntaaggoeqfff'


subjet = "Comprueba tu correo"
body = "Tengo algo que contarte!!"



em = EmailMessage()
em['From'] = sender
em['To'] = receiver
em['Subject'] = subjet

em.set_content(body)

contexto = ssl.create_default_context()

with smtplib.SMTP_SSL(server, port, context = contexto ) as s:
    s.login(sender,password)
    s.sendmail(sender,receiver,em.as_string())