'''
The module sends personalised email to provided email id with attachment.
'''
import smtplib
from email.message import EmailMessage

SENDER_EMAIL_ADDRESS = 'sender_email_address'
SENDER_EMAIL_PASSWORD = 'sender_email_password'
RECEIVER_EMAIL_ADDRESS = 'receiver_email_address'

msg = EmailMessage()
msg['Subject'] = 'Sucessfully initiated python learning'
msg['From'] = SENDER_EMAIL_ADDRESS 
msg['To'] = RECEIVER_EMAIL_ADDRESS 
msg.set_content('Hi, Please find attached python tutorial pdf.')

with open('python_tutorial.pdf', 'rb') as pdf:
    msg.add_attachment(pdf.read(), maintype='application', subtype='octet-stream', filename=pdf.name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(SENDER_EMAIL_ADDRESS, SENDER_EMAIL_PASSWORD) 
    smtp.send_message(msg)