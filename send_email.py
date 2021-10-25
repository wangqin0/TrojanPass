import os
import smtplib
import ssl
import logging

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# get Gmail credentials from system environment
ACCOUNT = os.getenv('TROJAN_PASS_GMAIL_ACCOUNT')
PASSWORD = os.getenv('TROJAN_PASS_GMAIL_PASSWORD')

PORT = 465  # Gmail Outgoing Mail (SMTP) Server
SMTP_SERVER = "smtp.gmail.com"


def send_from_gmail(recipient, subject, body, attachment_filepath, account, password):
    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = account
    message["To"] = recipient
    message["Subject"] = subject
    # message["Bcc"] = receiver_email  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    # Open PDF file in binary mode
    with open(attachment_filepath, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {attachment_filepath}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    logging.debug("Mail constructed, now sending")

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(account, password)
        server.sendmail(message["From"], message["To"], text)

    logging.debug("Mail sent")
