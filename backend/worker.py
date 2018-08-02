from celery import Celery
from search import process
import config 

# run with:
# $ redis-server
# $ celery -A worker worker --loglevel=debug

REDIS_BROKER_URL = getattr(config, 'REDIS_BROKER_URL')
app = Celery(__name__, backend='rpc://', broker=REDIS_BROKER_URL)

@app.task
def scrape_and_mail(keywords, email):
    try:
        return process(keywords, email)
    except Exception:
        return Exception
