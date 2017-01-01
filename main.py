from Query import Query
from Scraper import Scraper
import os


def form_url(url, page_number):
	return url+"/page/"+str(page_number)

def get_matching_posts(options):
	if query.is_limit:
		#read the webpage, pull out posts that match the criteria
		scraper.extract_matching_post_types(options)
		#remove the ones that exceed, underceed the character limit
		scraper.extract_posts_matching_char_limit(query.less_than, query.char_limit)

		scrapes.append(scraper.extracted_posts)

	else:
		#read the webpage, pull out posts that match the criteria
		scraper.extract_matching_post_types(options)
		scrapes.append(scraper.extracted_posts)


if __name__=="__main__":
	query_loop = True
	queries = []


	#Asks for the URLS of the blogs you'd like to scrape, along with the filters you'd like to scrape with
	while query_loop:
		proceed = input("Would you like to add another URL? (Y/N): ")
		if proceed == ("Y" or "y"):
			url = input("Please enter the url of the tumblr blog you'd like to scrape: ")
			limit = int(input("Please enter how many pages you would like to scrape (if all, put zero): "))

			query = Query(url, limit)
			query.choose_options()

			char_limit = input("Would you like a char limit? If not, leave empty. Ex. >200 (greater than 200 chars), <500 (less than 500 chars): ")
			query.choose_char_limit(char_limit)

			queries.append(query)
			
		else:
			query_loop = False

			
	#Scrapes the webpages
	for query in queries:
		scrapes = []
		if query.page_limit != 0:
			for page in range(query.page_limit):
				url = form_url(query.url, page+1)

				scraper = Scraper(url)
				get_matching_posts(query.options)
					

		else:
			count = 1
			url = form_url(query.url, count)
			scraper = Scraper(url)
			
			while scraper.has_content():
				get_matching_posts(query.options)
				count += 1
				url = form_url(query.url, count)
				scraper = Scraper(url)


	#Writes to file
	name = input("What would you like to name your file? ") + ".html"
	cwd = os.chdir(os.getcwd() + "/output")
	file = open(name, "w")
	file.truncate()
	for scrape in scrapes:
		file.write(str(scrape))



				

		

				
