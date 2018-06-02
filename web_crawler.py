from bs4 import BeautifulSoup as bs
import random
import requests
import time
from urllib.parse import (
    urljoin,
    urlparse,
)


pending = set()
crawled = []
start_domain = None


def get_html_from_url(url):
    r = requests.get(url)
    return r.text


def get_links_from_html(html):
    soup = bs(html, 'html.parser')
    return [link.get('href') for link in soup.find_all('a')]


def crawl_url(url):
    if urlparse(url).netloc != start_domain:
        return
    print('crawling {}'.format(url))
    time.sleep(random.uniform(1.0, 3.0))
    html = get_html_from_url(url)
    crawled.append(url)
    links = get_links_from_html(html)
    fully_qualified_links = [urljoin(url, link) for link in links]
    for link in fully_qualified_links:
        if link not in crawled:
            pending.add(link)


def crawl(start_url):
    global start_domain
    start_domain = urlparse(start_url).netloc
    pending.add(start_url)
    while pending:
        crawl_url(pending.pop())


if __name__ == '__main__':
    crawl('https://www.yoyowallet.com/')
    for link in crawled:
        print(link)
