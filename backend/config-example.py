# Mail configuration
SMTP_EMAIL = "smtp_email@domain.com"
SMTP_PASS = "smtp_pass"
MAIL_TEMPLATES = "util/mail_templates/"
# Logging configuration
LOGGING_DIR="log"
# Search/Scraper configuration
BASE_URL = "https://www.indeed.com"
NUM_PAGES = 5
DAYS_POSTED = 15
# Redis broker, production mode: redis://searchapp_redis_1:6379/, development mode: redis://localhost:6379/ 
REDIS_BROKER_URL = "redis://localhost:6379/"

