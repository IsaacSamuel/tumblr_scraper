from bs4 import BeautifulSoup
from urllib.request import urlopen


class Scraper:
    def __init__(self, url):
        html = urlopen(url).read()
        self.soup = BeautifulSoup(html, "lxml")
        
        
    def has_content(self):
        if self.soup.find_all(string=".post"):
            return True
        else:
            return False
        
