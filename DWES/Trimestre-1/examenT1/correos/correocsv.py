import ssl,smtplib,csv

message = "Subject: Hola {}, tu nota es {}"
sender = "santiDAW1234@gmail.com"
password = "bkrdntaaggoeqfff"

contexts = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com",465,context=contexts) as server:
    server.login(sender,password)
    with open('./contact_file.csv') as file:
        reader = csv.reader(file)
        next(reader)
        for name, email, grade in reader:
            server.sendmail(sender,email,message.format(name,grade))





