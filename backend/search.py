import requests
from bs4 import BeautifulSoup
import codecs
import os
import multiprocessing
from multiprocessing.pool import ThreadPool
import config 
from mail import Mailer
from logger import Logger

SMTP_EMAIL = getattr(config, 'SMTP_EMAIL')
SMTP_PASS = getattr(config, 'SMTP_PASS')
MAIL_TEMPLATES = getattr(config, 'MAIL_TEMPLATES')
MAILER = Mailer(SMTP_EMAIL, SMTP_PASS)
LOGGER = logger = Logger("search").get()

BASE_URL = getattr(config, 'BASE_URL')
NUM_PAGES = getattr(config, 'NUM_PAGES')
POOL_SIZE = multiprocessing.cpu_count()
DAYS_POSTED = getattr(config, 'DAYS_POSTED')

def get_links(base_url, n, search_terms):
    links = []
    for i in range(0,n):
        for search in search_terms:
            links.append(BASE_URL + '/jobs?q='+search+'&l=Charlotte%2C+NC&start=0' + str(i) + '&jt=fulltime')
    return links

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
                        return { 'title': ahref['title'], 'url': BASE_URL + ahref['href'] }

def create_body(posts, to_mail):
    LOGGER.info("Begin mail creation...")
    f = codecs.open(os.path.join(MAIL_TEMPLATES + 'job_suggestions.html'), 'r')
    soup = BeautifulSoup(f.read(), "lxml")
    # To email response
    mailTo = soup.find("b", {"id": "email"})
    mailTo.insert(0, str(to_mail.split("@")[0]))
    # Table fill with listings
    tableBody = soup.find("tbody", {"id": "listingsBody"})
    for post_dict in posts:
        row = BeautifulSoup('''
                            <tr>
                                <td><p class="listing">{}</p></td>
                                <td><a class="listingLink" href="{}" target="_blank">View</a></td>
                            </tr> 
                        '''.format(post_dict.get('title', None), post_dict.get('url', None)), "lxml")
        rowContents = row.html.body.tr
        tableBody.insert(0, rowContents)
    
    LOGGER.info("Created mail body...")
    return soup

def process(search_terms, to_email):
    try:
        LOGGER.info("Starting web scrape...")
        # generate links to process
        links = get_links(BASE_URL, NUM_PAGES, search_terms)
        # split into pool of threads to process
        with ThreadPool(POOL_SIZE) as p:
            all_posts = p.map(get_posts, links)
            p.terminate()
            cleaned_posts = list(post_dict for post_dict in all_posts if post_dict is not None)
            unique_posts = list(values for key, values in enumerate(cleaned_posts) if values not in cleaned_posts[key + 1:])
            mail_body = create_body(unique_posts, to_email)
            MAILER.send_mail("Job Postings Based on Your Resume", mail_body, to_email)
            LOGGER.info("Successfully processed listings")
            return True
    except Exception as e:
        LOGGER.exception(str(e))
        raise e
