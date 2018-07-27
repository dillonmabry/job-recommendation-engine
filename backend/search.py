import requests
import datetime
import time
from bs4 import BeautifulSoup
import multiprocessing
from multiprocessing.pool import ThreadPool
import config 
from mail import Mailer
from logger import Logger

FROM_EMAIL = getattr(config, 'FROM_EMAIL')
TO_EMAIL = getattr(config, 'TO_EMAIL')
SMTP_PASS = getattr(config, 'SMTP_PASS')
MAILER = Mailer(FROM_EMAIL, TO_EMAIL, SMTP_PASS)
LOGGER = logger = Logger("search").get()

BASE_URL = getattr(config, 'BASE_URL')
NUM_PAGES = getattr(config, 'NUM_PAGES')
POOL_SIZE = multiprocessing.cpu_count()-1
DAYS_POSTED = getattr(config, 'DAYS_POSTED')

# get/generate links to parse
def get_links(base_url, n, search_terms):
    links = []
    for i in range(0,n):
        for search in search_terms:
            links.append(BASE_URL + '/jobs?q='+search+'&l=Charlotte%2C+NC&start=0' + str(i) + '&jt=fulltime')
    return links

# get list of posts via text
def get_posts(url):
    r = requests.get(url)
    bsoup = BeautifulSoup(r.text, "html.parser")
    posts = bsoup.findAll(True, {"class":["row", "result","clickcard"]})
    for post in posts:
        days_posted = post.find("span", {"class":"date"})
        if days_posted is not None:
            days = int(days_posted.getText()[:2])
            if days < DAYS_POSTED:
                heading = post.find("h2", {"class":"jobtitle"})
                if heading is not None:
                    ahref = heading.find('a', href=True)
                    if ahref is not None:
                        return BASE_URL + ahref['href']

def process(search_terms):
    try:
        LOGGER.info("Starting web scrape...")
        start_time = time.time()
        # generate links to process
        links = get_links(BASE_URL, NUM_PAGES, search_terms)

        # split into pool of threads to process
        with ThreadPool(POOL_SIZE) as p:
            all_posts = p.map(get_posts, links)
            unique_posts = set(all_posts) # ensure unique postings
            p.terminate()
            joined_posts = '\n\n'.join([str(post) for post in unique_posts if post is not None])
            MAILER.send_mail("JOB POSTINGS AS OF "+str(datetime.datetime.now()),  joined_posts)
            LOGGER.info("Successfully processed listings")
            return True
    except Exception as e:
        LOGGER.exception(str(e))
        raise e
