from Query import Query

if __name__=="__main__":
    query_loop = True
    queries = []

    while query_loop:
        proceed = input("Would you like to add another URL? (Y/N): ")
        if proceed == "Y" or "y":
            url = input("Please enter the url of the tumblr blog you'd like to scrape: ")
            limit = int(input("Please enter how many pages you would like to scrape (if all, put zero): "))

            query = Query(url, limit)
            query.choose_options()

            char_limit = input("Would you like a char limit? If not, leave empty. Ex. >200 (greater than 200 chars), <500 (less than 500 chars): ")
            query.choose_char_limit(char_limit)
            
        else:
            query_loop = false
    

    
