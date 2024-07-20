# import smtplib library

import smtplib 
# # #create a object of smtp class and provide host of smtp server we use gmail and give port no.
server=smtplib.SMTP("smtp.gmail.com",587)

# # #start encrypted connection
#tls---> transfer the data with sequrity
server.starttls()

# # #login  use sender email and password(not a right way to show password openly)
server.login("choudharyshalu598@gmail.com","shalu@2004")

# Subject="program of sending email"
# name="shalu choudhary"
# college="government women engineering college"
# city="Ajmer"

# message="Subject:{}\n\n{}\n\n{}".format(name,college,city)
# print(message)

