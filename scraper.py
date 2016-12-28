from bs4 import BeautifulSoup
from urllib.request import urlopen


def select_options():
    option_loop = True
    options = {
        "url" = ""
        "limit" = 0
        "text" = False
        "image" = False
        "video" = False
        "quote" = False
        "chat" = False
        "less_than" = False
        "char_lim" = 0
        }
    

    options["url"] = input("Please enter the url of the tumblr blog you'd like to scrape: ")

    option["limit"] = input("Please enter how many pages you would like to scrape (if all, put zero): ")

    print("Options are: text, image, video, quote, or chat.")    
    while option_loop:
        option = [input("Please enter your options; type done when done.")]
        if option = "text":
            options["text"] = True
        if option = "image":
            options["image"] = True
        if option = "video":
            options["video"] = True
        if option = "quote":
            options["quote"] = True
        if option = "chat":
            options["chat"] = True

    char_limit = input("Would you like a char limit? If not, leave empty. Ex. >200 (greater than 200 chars), <500 (less than 500 chars): ")
    if char_limit != "":
        if char_limit[0] = "<":
            options["less_than"] = True
        else if char_limit[0] = ">":
            options["less_than"] = False
        option["char_lim"] = int(char_limit[1, -1])

    return options


if __name__=="__main__":
    query = select_options()

    
    
    
    
