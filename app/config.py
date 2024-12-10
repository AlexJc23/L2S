import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    FLASK_RUN_PORT = os.environ.get('FLASK_RUN_PORT')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.gmail.com'  # or your SMTP server
    MAIL_PORT = 465  # for SSL, or use 587 for TLS
    MAIL_USE_SSL = True  # or False for TLS
    MAIL_USE_TLS = False
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')  # Use app-specific password
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_USERNAME')  # Default sender email address
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')  # OpenAI API Key

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace('postgres://', 'postgresql://')
    SQLALCHEMY_ECHO = True
