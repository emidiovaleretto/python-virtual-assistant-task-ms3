import ssl
import smtplib
from environs import Env
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Create an Env object
env = Env()
env.read_env()

host = env("HOST")
port = env("PORT_GMAIL")
sender_email = env("EMAIL_ADDRESS")
password = env("PASSWORD")


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
            "\nCouldn't connect. There may be a problem with "
            "the server. Please try again later."
        )
        return False

    return True
