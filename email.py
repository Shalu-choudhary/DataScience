import smtplib
sen_email=input("sender email")
rec_mail=input("reciver email")

subject=input("Subject:")
message=input("Message : ")

text=f"Subject: {subject}\n\n{message}"

server=smtplib.SMTP("smtp.gmail.com",587)

server.starttls()
server.login(sen_email,"adix fptm phim aqcl")
server.sendmail(sen_email,rec_mail,text)

print("email sent to the "+rec_mail)
server.quit()
