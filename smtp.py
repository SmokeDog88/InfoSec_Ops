# Written by Miguel Bigueur
# Email Interactions using smtp
# Security Scripting w/Python
# Dec 24, 2017

import smtplib
from email.mime.text import MIMEText

ehlo foo.com
mail from:  foo@foo.com
rcpt to:  me@me.com
data

s = smtplib.SMTP("domain", 25)
s.login("user", "password")

try:
     file = open("myfile", "r")
     m = MIMEText(file.read())
     file.close()

     m['To'] = "To@data.com"
     m['From'] = "From_me@gmail.com"
     m['Subject'] = "Your data message"

     s.send_message(m)
     print("Finished sending File")

except Exception as e:
    print("Unable to send File: ", e)

s.quit()
