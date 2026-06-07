from email.message import EmailMessage
import smtplib

msg=EmailMessage()

msg["subject"]="Python Test"
msg["From"]="hometvs1982@gmail.com"
msg["To"]=("apurvasawant1827@gmail.com","sapurva23cs@student.mes.ac.in")

msg.set_content("""Hello,
                This is python email test Regards,
                Apurva """)

# msg.add_alternative("""html code """,subtype="html")
# msg.add_attachment()#For pdf or file document

with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
  #SMTP_SSL-Secure from the start
  smtp.login(
    "hometvs1982@gmail.com",
    "wcvm dsyc mqde nzgb"
  )
  
  smtp.send_message(msg)
print("Email sent!")


