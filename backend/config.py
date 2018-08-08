import os
from dotenv import load_dotenv
load_dotenv()

SMTP_EMAIL = os.environ.get('SMTP_EMAIL')
SMTP_PASS = os.environ.get('SMTP_PASS')
MAIL_TEMPLATES = os.environ.get('MAIL_TEMPLATES')
LOGGING_DIR= os.environ.get('LOGGING_DIR')
BASE_URL = os.environ.get('BASE_URL')
NUM_PAGES = int(os.environ.get('NUM_PAGES'))
DAYS_POSTED = int(os.environ.get('DAYS_POSTED'))
REDIS_BROKER_URL = os.environ.get('REDIS_BROKER_URL')
