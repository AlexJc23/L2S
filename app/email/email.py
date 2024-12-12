from flask_mail import Message, Mail
from flask import Flask
import os
from dotenv import load_dotenv
import traceback

# Load environment variables
load_dotenv()

# Initialize Flask app and Mail
app = Flask(__name__)
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USE_TLS=False,
    MAIL_USERNAME=os.environ.get('MAIL_USERNAME'),
    MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD'),
    MAIL_DEFAULT_SENDER=os.environ.get('MAIL_USERNAME'),
)
mail = Mail(app)

def send_santa_email(user_email, santa_message):
    """
    Send a message from Santa to the specified user email.
    """
    print(f"Preparing to send email to: {user_email}")
    msg = Message(
        subject="A Special Message from Santa",
        sender=os.environ.get('MAIL_USERNAME'),
        recipients=[user_email],
        body=santa_message,
    )
    try:
        with app.app_context():  # Ensure Flask context is active
            mail.send(msg)
        print(f"Email successfully sent to {user_email}")
    except Exception as e:
        print(f"Failed to send email to {user_email}. Error: {str(e)}")
        traceback.print_exc()  # Print the full traceback for debugging
