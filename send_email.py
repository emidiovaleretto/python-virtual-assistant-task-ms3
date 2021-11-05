import smtplib
import ssl
from decouple import config

host = config("HOST")
port = config("PORT")
email_address = config("EMAIL_ADDRESS")
password = config("PASSWORD")

# Create a secure SSL context
context = ssl.create_default_context()


def send_email(user_email_address, message):
    """
    This function sends an email from the email
    address specified in the config file to the
    email address specified in the function call.
    The message will be the conversation log.
    """

    try:
        with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
            server.login(email_address, password=password)
            server.sendmail(
                to_addrs=user_email_address,
                from_addr=email_address,
                msg=message,
            )
            server.quit()

    except Exception:
        print(
            "Sorry. It appears that you have not entered "
            "your email address correctly."
        )
        return False
