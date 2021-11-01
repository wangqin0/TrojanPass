import os
import smtplib
import ssl
import logging

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

PORT = 465  # Gmail Outgoing Mail (SMTP) Server
SMTP_SERVER = "smtp.gmail.com"


class EmailManager:
    def __init__(self, account: str, password: str):
        context = ssl.create_default_context()
        self.account = account
        self.server = smtplib.SMTP_SSL(SMTP_SERVER, PORT, context=context)
        self.server.login(account, password)

    def send_email(self, email: MIMEMultipart):
        recipient = email['To']
        self.server.sendmail(self.account, recipient, email.as_string())
        logging.debug("Mail sent")

    @staticmethod
    def construct_email(_from: str, _to: str, subject: str, content: str, attachment_dir: str = None) -> MIMEMultipart:
        # Create a multipart message and set headers
        email = MIMEMultipart()
        email["From"] = _from
        email["To"] = _to
        email["Subject"] = subject

        # Add body to email
        email.attach(MIMEText(content, "plain"))

        if attachment_dir:
            # Open PDF file in binary mode
            with open(attachment_dir, "rb") as attachment:
                # Add file as application/octet-stream
                # Email client can usually download this automatically as attachment
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())

                # Encode file in ASCII characters to send by email
                encoders.encode_base64(part)

                # Add header as key/value pair to attachment part
                part.add_header(
                    "Content-Disposition",
                    f"attachment; filename= {attachment_dir}",
                )

                # Add attachment to message and convert message to string
                email.attach(part)

        return email
