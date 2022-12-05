import smtplib, ssl

reciver = 'santiDAW1234@gmail.com'
sender = 'santiDAW1234@gmail.com'
message = 'Subject: Hola, que tal'
password = 'bkrdntaaggoeqfff'

contexts = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=contexts) as server:
    server.login(sender,password)
    server.sendmail(sender,reciver,message)