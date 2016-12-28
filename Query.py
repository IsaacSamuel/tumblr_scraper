class Query:

    def __init__(self, url, page_limit):
        self.url = url
        self.page_limit = page_limit

    def choose_options(self):
        print("Options are: text, image, video, quote, or chat.")
        self.text = False
        self.image = False
        self.video = False
        self.quote = False
        self.chat = False
        
        option_loop = True
        
        while option_loop:
            option = input("Please enter your options; type done when done: ")
            if option == "text":
                self.text = True
            if option == "image":
                self.image = True
            if option == "video":
                self.video = True
            if option == "quote":
                self.quote = True
            if option == "chat":
                self.chat = True
            if option == "done":
                option_loop = False

    def choose_char_limit(self, char_lim):
        less_than = False
        
        if char_lim != "":
            if char_lim[0] == "<":
                self.less_than = True
            elif char_lim[0] == ">":
                self.less_than = False
                
            self.char_limit = int(char_lim[1, -1])  
            return True
        
        else:
            return False

        
