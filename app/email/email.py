from flask_mail import Message, Mail
from flask import current_app

# Initialize Flask-Mail
mail = Mail()

def send_santa_email(user_email, santa_message):
    """
    Send the Santa message via email
    """
    msg = Message("A Special Message from Santa",
                  recipients=[user_email],
                  body=santa_message)
    try:
        mail.send(msg)
        print(f"Message sent to {user_email}")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")
