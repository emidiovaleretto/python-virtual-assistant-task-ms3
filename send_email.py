import smtplib
import ssl
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from decouple import config


host = config("HOST")
port = config("PORT")
sender_email = config("EMAIL_ADDRESS")
password = config("PASSWORD")


def send_email(receiver_email):
    """
    This function sends an email from the email
    address specified in the config file to the
    email address specified in the function call.
    The message will be the conversation log.
    """

    message = MIMEMultipart()
    message["Subject"] = "Your conversation log"
    message["From"] = "Python Bot"
    message["To"] = receiver_email

    # Create the plain-text version of message
    body = """
Hi!

How are you doing today?
Thanks for using our service.

Please see attached file for the above mentioned subject.

Yours sincerely,
Python Bot
"""

    # Add body to message
    message.attach(MIMEText(body, "plain"))

    # Create a secure SSL context
    context = ssl.create_default_context()

    file = "log.txt"

    with open(file, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read(), "base64")

    # Add headers as key/value pairs to attachment part
    part.add_header("Content-Disposition", f"attachment; filename= {file}")

    message.attach(part)

    try:
        with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
            server.login(sender_email, password=password)
            print("\nOne moment, please.")
            server.sendmail(
                to_addrs=receiver_email,
                from_addr=sender_email,
                msg=message.as_string(),
            )
            server.quit()

    except Exception:
        print(
            "Sorry. It appears that you have not entered "
            "your email address correctly."
        )
        return False

    return True
