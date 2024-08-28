from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'albite.tech23@gmail.com'
email_password = 'gwuo lthp pijt hbmz'

email_receiver = []
email_bcc = ['rigoja6977@dalebig.com', 'sanketu2141@gmail.com', 'albite.tech23@gmail.com']

subject = 'Subscribe to our newsletter.'
body = """
Need latest updates first and on your fingertips.
Subscribe.
"""

em=EmailMessage()
em['From']= email_sender
em['To']= ','.join(email_receiver)
em['subject']= subject
em.set_content(body)

all_recipients = email_receiver + email_bcc

context= ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, all_recipients, em.as_string())

print("Email sent successfully.")





