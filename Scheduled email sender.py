import schedule
print(schedule.__version__)

import time
from email.message import EmailMessage
import ssl
import smtplib

# Email configuration
email_sender = 'albite.tech23@gmail.com'
email_password = 'gwuo lthp pijt hbmz'

# Recipients
email_receiver = ['rigoja6977@dalebig.com', 'sanketu2141@gmail.com']
email_bcc = ['bcc1@example.com', 'bcc2@example.com']

subject = 'Subscribe to our newsletter.'
body = """
Need latest updates first and on your fingertips.
Subscribe.
"""

def send_email():
    # Create email message
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = ', '.join(email_receiver)
    em['Subject'] = subject
    em.set_content(body)

    # Combine all recipients (To and BCC)
    all_recipients = email_receiver + email_bcc

    # Create SSL context
    context = ssl.create_default_context()

    # Send email
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, all_recipients, em.as_string())
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Schedule the email to be sent daily at a specific time
schedule.every().day.at("08:00").do(send_email)  # Change "08:00" to your desired time in 24-hour format

while True:
    schedule.run_pending()
    time.sleep(1)
