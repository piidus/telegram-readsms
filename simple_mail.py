import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from email.header import Header
import os
from dotenv import load_dotenv
load_dotenv()
mail_id =os.environ.get('mail_id')
mail_pwd =os.environ.get('mail_pwd')
mail_server =os.environ.get('mail_server')
mail_receiver =os.environ.get('mail_receiver')


def send_email(subject, message, from_email, to_email, smtp_server, smtp_port, smtp_username, smtp_password):
    # Create a message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Add body to the message
    msg.attach(MIMEText(message, 'plain'))

    try:
        # Establish a connection to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Upgrade the connection to secure (TLS) mode
        server.login(smtp_username, smtp_password)

        # Send the email
        server.sendmail(from_email, to_email, msg.as_string())
        print("Email sent successfully!")

    except Exception as e:
        print("Error sending email:", e)

    finally:
        # Close the connection to the SMTP server
        server.quit()

# Example usage
subject = 'Test Email'
message = 'This is a test email sent using smtplib.'
from_email = mail_id
to_email = mail_receiver
smtp_server = mail_server
smtp_port = 587  # Port for TLS (587 for Gmail)
smtp_username = mail_id
smtp_password = mail_pwd

send_email(subject, message, from_email, to_email, smtp_server, smtp_port, smtp_username, smtp_password)
