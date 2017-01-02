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


	"""
	Will implement sorting by date later. Use datetime module.
	def extract_date(self, post):
		soup = BeautifulSoup(str(post), 'lxml')
		for each in soup.find_all("div", {"class" : "date"}):
			self.extracted_posts.append(each)
	"""


	def extract_matching_post_types(self, options):
		self.extracted_posts= []
		if options["text"]:
			for post in self.soup.find_all("div", {"class" : "post post-type-text"}):
				self.extracted_posts.append(post)
		if options["image"]:
			for post in self.soup.find_all("div", {"class" : "post post-type-image"}):
				self.extracted_posts.append(post)
		if options["video"]:
			for post in self.soup.find_all("div", {"class" : "post post-type-video"}):
				self.extracted_posts.append(post)
		if options["chat"]:
			for post in self.soup.find_all("div", {"class" : "post post-type-chat"}):
				self.extracted_posts.append(post)
		if options["quote"]:
			for post in self.soup.find_all("div", {"class" : "post post-type-quote"}):
				self.extracted_posts.append(post)


	def extract_posts_matching_char_limit(self, less_than, char_lim):
		temp_posts = self.extracted_posts
		self.extracted_posts = []

		for post in temp_posts:
			soup = BeautifulSoup(str(post), 'lxml')
			for each in soup.find_all("div", {"class" : "post-content"}):
				if less_than:
					if len(str(each)) <= (char_lim + 7):
						self.extracted_posts.append(post)
				if not less_than:
					if len(str(each)) <= (char_lim + 7):
						self.extracted_posts.append(post)


