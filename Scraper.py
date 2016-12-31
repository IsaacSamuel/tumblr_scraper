from bs4 import BeautifulSoup
from bs4 import Comment
import requests



class Scraper:
	posts_found = 0

	def __init__(self, url):
		html = requests.get(url, verify=False).content
		self.soup = BeautifulSoup(html, "lxml")


	#If the user elects to scrape an entire blog, we need to check when the blog has run out of page. 
	#We do this by checking if a page contains a comment labled ' .post '
	def has_content(self):
		for comment in self.soup.find_all(text=lambda text:isinstance(text, Comment)):
			if comment == " .post ":
				return True
		return False


	def extract_matching_post_types(self, options):
		self.extracted_posts= []
		if options["text"]:
			for post in self.soup.find_all("div", {"class" : "post post-type-text"}):
				self.extracted_posts.appends(post)
		if options["image"]:
			for post in self.soup.find_all("div", {"class" : "post post-type-image"}):
				self.extracted_posts.appends(post)
		if options["video"]:
			for post in self.soup.find_all("div", {"class" : "post post-type-video"}):
				self.extracted_posts.appends(post)
		if options["chat"]:
			for post in self.soup.find_all("div", {"class" : "post post-type-chat"}):
				self.extracted_posts.appends(post)
		if options["quote"]:
			for post in self.soup.find_all("div", {"class" : "post post-type-quote"}):
				self.extracted_posts.appends(post)
		
