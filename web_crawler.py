from bs4 import BeautifulSoup as bs
import requests


pending = []
crawled = []


def get_html_from_url(url):
    r = requests.get(url)
    return r.text


def get_links_from_html(html):
    soup = bs(html, 'html.parser')
    return [link.get('href') for link in soup.find_all('a')]
