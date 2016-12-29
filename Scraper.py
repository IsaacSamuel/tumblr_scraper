from bs4 import BeautifulSoup
from bs4 import Comment
import requests



class Scraper:
	def __init__(self, url):
		html = requests.get(url, verify=False).content
		self.soup = BeautifulSoup(html, "lxml")

	def has_content(self):
		for comment in self.soup.find_all(text=lambda text:isinstance(text, Comment)):
			if comment == " .post ":
				return True
		return False

	def extract_matching_options(self, options):
		print("Worked!")
		
