class Query:

	def __init__(self, url, page_limit):
		self.url = url
		self.page_limit = page_limit

	def choose_options(self):
		print("Options are: text, image, video, quote, or chat.")
		self.options = {
			"text": False,
			"image": False,
			"video": False,
			"quote": False,
			"chat": False
			}
		
		option_loop = True
		
		while option_loop:
			option = input("Please enter your options; type done when done: ")
			if option == "text":
				self.options["text"] = True
			if option == "image":
				self.options["image"] = True
			if option == "video":
				self.options["video"] = True
			if option == "quote":
				self.options["quote"] = True
			if option == "chat":
				self.options["chat"] = True
			if option == "done":
				option_loop = False

	def choose_char_limit(self, char_lim):
		self.less_than = False
		self.char_limit = 0

		if char_lim is not "":
			if char_lim[0] == "<":
				self.less_than = True
			elif char_lim[0] == ">":
				self.less_than = False
			else:
				raise TypeError
			
			self.char_limit = int(char_lim[1:])
			self.is_limit = True

		else:
			self.is_limit = False
		
