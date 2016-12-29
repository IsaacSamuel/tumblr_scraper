from Query import Query

if __name__=="__main__":
    query_loop = True
    queries = []


    #Asks for the URLS of the blogs you'd like to scrape, along with the filters you'd like to scrape with
    while query_loop:
        proceed = input("Would you like to add another URL? (Y/N): ")
        if proceed == "Y" or "y":
            url = input("Please enter the url of the tumblr blog you'd like to scrape: ")
            limit = int(input("Please enter how many pages you would like to scrape (if all, put zero): "))

            query = Query(url, limit)
            query.choose_options()

            char_limit = input("Would you like a char limit? If not, leave empty. Ex. >200 (greater than 200 chars), <500 (less than 500 chars): ")
            query.choose_char_limit(char_limit)

            queries.append(query)
            
        else:
            query_loop = false

            
    #Scrapes the webpages
    for query in queries:
        
        if query.page_limit != 0:
            for page in query.page_limit:
                url = form_url(query.url, page+1)

                scraper = Scraper(url)

                get_matching_posts(query.options, query.is_limit, query.less_than, query.char_limit):
                    

        else:
            count = 1
            url = form_url(query.url, count)

            scraper = Scraper(url)
            
            while scraper.has_content()
                url = form_url(query.url, count)
                get_matching_posts(query.options, query.is_limit, query.less_than, query.char_limit):
                    


def form_url(url, page_number):
    if query.page_limit:
        return page.url+"/page/"+(page_number)
    else:
        return page.url+"/page/"+(page_number)

def get_matching_posts(query.options, query.is_limit, query.less_than, query.char_limit):
    if query.is_limit():
        #read webpage, pull out links with criteria
        scraper.extract_matching_options(self.options)
        #remove the ones that exceed, underceed the character limit

    else:
        #read the webpage, pull out links with criteria
        scraper.extract_matching_options(self.options)
                        

        

                
