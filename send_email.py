import ssl
import smtplib
from environs import Env
from time import sleep
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pyisemail import is_email


# Create an Env object
env = Env()
env.read_env()

host = env("HOST")
port = env("PORT_GMAIL")
sender_email = env("EMAIL_ADDRESS")
password = env("PASSWORD")


def validate_email_address(email_address):
    """
    This function validates the email address
    passed to it.
    """

    try:
        is_a_valid_email = is_email(email_address, check_dns=True)
        return is_a_valid_email

    except ValueError as err:
        print(str(err))
        return False


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

    is_a_valid_email = validate_email_address(receiver_email)

    if is_a_valid_email:

        try:
            with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
                server.login(sender_email, password=password)
                server.sendmail(
                    to_addrs=receiver_email,
                    from_addr=sender_email,
                    msg=message.as_string(),
                )
                print("\nOne moment, please.")
                sleep(3)
                print("\nSending email...\n")
                sleep(5)
                server.quit()

        except Exception:
            print(
                "\nCouldn't connect. There may be a problem with "
                "the server. Please try again later."
            )
            return False

    else:
        sleep(3)
        print(
            "Sorry. It appears that you have not entered "
            "your email address correctly.\n"
        )
        return False

    return True
