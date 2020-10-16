import smtplib
from email.mime.text import MIMEText

body = "this is test email how are you :D"

msg = MIMEText(body)
msg['From'] = "@.com"
msg['To']="@.com"
msg['Subject']="Hello"

server = smtplib.SMTP('smtp..com',)
server.starttls()
server.login("", "")
server.send_message(msg)

print("mail sent")

server.quit()