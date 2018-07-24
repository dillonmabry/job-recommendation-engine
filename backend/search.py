import requests
import datetime
import time
from bs4 import BeautifulSoup
import multiprocessing
from multiprocessing.pool import ThreadPool
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Config
import config 
FROM_EMAIL = getattr(config, 'FROM_EMAIL')
TO_EMAIL = getattr(config, 'TO_EMAIL')
SMTP_PASS = getattr(config, 'SMTP_PASS')

BASE_URL = 'https://www.indeed.com'
NUM_PAGES = 5
POOL_SIZE = multiprocessing.cpu_count()-1
DAYS_POSTED = 15

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

def send_mail(posts):
    fromaddr = FROM_EMAIL
    toaddr = TO_EMAIL
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "JOB POSTINGS AS OF "+str(datetime.datetime.now())

    body = '\n\n'.join([str(x) for x in posts])
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP_SSL('smtp.gmail.com:465')
    server.login(fromaddr, SMTP_PASS)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

def search(search_terms):
    try:
        print("Processing...")
        start_time = time.time()
        # generate links to process
        links = get_links(BASE_URL, NUM_PAGES, search_terms)

        # split into pool of threads to process
        with ThreadPool(POOL_SIZE) as p:
            all_posts = p.map(get_posts, links)
            unique_posts = set(all_posts)
            print("--- Finished processing in %s seconds ---" % (time.time() - start_time))
            p.terminate()
            send_mail(unique_posts)
            print("--- Mail Sent ---")
            return True
    except Exception as e:
        return str(e)
