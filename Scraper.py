from bs4 import BeautifulSoup
from urllib.request import urlopen


class Scraper:

    def __main__(self):
    
    def make_soup(self, url):
        html = urlopen(url).read()
        return BeautifulSoup(html, "lxml")
        
    def check_page_number(self, limit):
        
