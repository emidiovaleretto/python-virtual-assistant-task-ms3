import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from decouple import config


host = config("HOST")
port = config("PORT")
sender_email = config("EMAIL_ADDRESS")
password = config("PASSWORD")


def send_email(receiver_email, content):
    """
    This function sends an email from the email
    address specified in the config file to the
    email address specified in the function call.
    The message will be the conversation log.
    """

    message = MIMEMultipart("alternative")
    message["Subject"] = "Your conversation log"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text version of message
    text = f"""
Hi!
How are you doing today?
Thanks for using our service.
Here is your conversation log: \n{content}
"""

    # Turn the message into a html MIMEText object
    part1 = MIMEText(text, "plain")

    # Attach the plain-text part to the MIMEMultipart object
    message.attach(part1)

    # Create a secure SSL context
    context = ssl.create_default_context()

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
