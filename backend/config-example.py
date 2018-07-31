# Mail configuration
FROM_EMAIL = "from_example.com"
TO_EMAIL = "to_example.com"
SMTP_PASS = "smtp_pass"
# Logging configuration
LOGGING_DIR="log"
# Search/Scraper configuration
BASE_URL = "https://www.indeed.com"
NUM_PAGES = 5
DAYS_POSTED = 15
# Redis queue, based on docker-compose main .env config
REDIS_BROKER_URL = 'redis://searchapp_redis_1:6379/'

