import shutil
import smtplib
import time
from email.message import EmailMessage

GB = 1024 * 1024 * 1024
free = shutil.disk_usage('/').free // (2**30)
total = shutil.disk_usage('/').total // (2**30)

percent = " "   #  it mails you when free disk percent lower than this.
delay = " " #  in seconds


msg= EmailMessage()
my_address ="   "    #sender address
app_generated_password = "  "    # gmail generated password
msg["Subject"] = "   "   #email subject 
msg["From"]= my_address      #sender address
msg["To"] = "   "     #reciver address
msg.set_content("  ")   #message body

while True:
    time.sleep(int(delay))
    if free < total*(int(percent)/100):
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(my_address,app_generated_password)    #login gmail account
            smtp.send_message(msg)   #send message 
