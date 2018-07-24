from celery import Celery
from search import search

# run with:
# $ redis-server
# $ celery -A worker worker --loglevel=debug

app = Celery(__name__, backend='rpc://', broker='redis://localhost:6379/')

@app.task
def scrape_and_mail(keywords):
    try:
        return search(keywords)
    except Exception:
        return Exception
