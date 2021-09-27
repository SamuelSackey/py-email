import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Samuel Sackey'
email['to'] = 'leonardscky@gmail.com'
email['subject'] = 'Hello World!'

email.set_content('Welcome to this big wide world!')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('smlscky@gmail.com', '************')
    smtp.send_message(email)
    print('Email sent successfully')
