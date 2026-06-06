import smtplib

sender = "hometvs1982@gmail.com"
receiver ="apurvasawant1827@gmail.com"
password="wcvm dsyc mqde nzgb"

subject="Python test"

body=""" Hi,

        This email was automatically sent using python,
        Thank you
        Regards
        Apurva
"""

message=f"subject:{subject}\n\n{body}"


server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()

server.login(sender,password)
server.sendmail(sender,receiver,message)

print("Email sent!")