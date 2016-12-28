class Query:

    def __init__(self, url, page_limit):
        self.url = url
        self.page_limit = page_limit

    def choose_options():
        print("Options are: text, image, video, quote, or chat.")
        self.text = False
        self.image = False
        self.video = False
        self.quote = False
        self.chat = False
        
        option_loop = True
        
        while option_loop:
            option = [input("Please enter your options; type done when done.")]
            if option == "text":
                options["text"] = True
            if option == "image":
                options["image"] = True
            if option == "video":
                options["video"] = True
            if option == "quote":
                options["quote"] = True
            if option == "chat":
                options["chat"] = True
            if option == "done":
                option_loop = false

    def choose_char_limit(char_lim):
        less_than = False
        
        if char_limit != "":
            if char_limit[0] = "<":
                self.less_than = True
            else if char_limit[0] = ">":
                self.less_than = False
            self.char_limit = int(char_limit[1, -1])

        
