import os

# *****************************
# Environment specific settings
# *****************************

# DO NOT use "DEBUG = True" in production environments
DEBUG = True

# DO NOT use Unsecure Secrets in production environments
# Generate a safe one with:
#     python -c "import os; print repr(os.urandom(24));"
#SECRET_KEY = 'This is an UNSECURE Secret. CHANGE THIS for production environments.'
SECRET_KEY = os.getenv('SECRET_KEY')

# SQLAlchemy settings
#SQLALCHEMY_DATABASE_URI = 'sqlite:///../app.sqlite'
#SQLALCHEMY_DATABASE_URI = 'sqlite:////Users/markhallett/notgoogledrive/github/mysite/app.sqlite'
SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')

# Flask-Mail settings
# For smtp.gmail.com to work, you MUST set "Allow less secure apps" to ON in Google Accounts.
# Change it in https://myaccount.google.com/security#connectedapps (near the bottom).
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_SSL = False
MAIL_USE_TLS = True
MAIL_USERNAME = os.getenv('GMAIL_USERNAME')
MAIL_PASSWORD = os.getenv('GMAIL_PASSWORD')
MAIL_DEFAULT_SENDER = '"Register" <medaredaltd@gmail.com>'

ADMINS = [
    '"Admin One" <admin1@gmail.com>',
    ]
