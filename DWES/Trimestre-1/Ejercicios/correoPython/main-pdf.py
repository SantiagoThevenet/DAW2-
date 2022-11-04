import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
port = 465
sender_mail = "Private Person <from@example.com>"
receiver_mail = "A Test User <to@example.com>"
server_domain = "smtp.mailtrap.io"
subject = "Mail con adjunto"
body = "Esto es un mensaje con archivo adjunto Python."
message = MIMEMultipart()
message["Subject"] = subject
message["From"] = sender_mail
message["To"] = receiver_mail
message["Bcc"] = receiver_mail
message.attach(MIMEText(body, "plain"))
filename = "../../PDFs/Introducción a los subprocesos.pdf"
with open(filename, 'rb') as f:
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(f.read())
encoders.encode_base64(part)
part.add_header("Content-Disposition",
 "atachment;filename={}".format(filename))
message.attach(part)
text = message.as_string()
context = ssl.create_default_context()
with smtplib.SMTP(server_domain, port) as s:
 s.login("84ebdfe2003e7e", "00097932a0ac18")
 s.sendmail(sender_mail, receiver_mail, text)
print("Email enviado!!!")