import os
parent_directory = os.path.abspath("..")
import sys
sys.path.append(parent_directory)

from Scraper import Scraper
from Query import Query

import unittest

class Query_char_limit_good_input(unittest.TestCase):

	#Functions for tests
	#creates dummy query, calls choose_char_limit, collects object vals in a dictionary
	def set_test_vals(self, char_limit):
		query = Query("www.whatever.com", 0)

		query.choose_char_limit(char_limit)

		self.query_vals = {
			"is_limit" : query.is_limit,
			"less than" : query.less_than,
			"value" : query.char_limit
		}


	#Tests
	#Test should pass when user inputs nothing
	def test_no_input(self):
		no_input = {
			"is_limit" : False,
			"less than" : False,
			"value" : 0
		}

		self.set_test_vals("")

		self.assertEqual(no_input, self.query_vals)


	#Test should pass when user inputs >200
	def test_greater_than(self):
		above_200 = {
			"is_limit" : True,
			"less than" : False,
			"value" : 200
		}

		self.set_test_vals(">200")

		self.assertEqual(above_200, self.query_vals)


	#Test should pass when user inputs <200
	def test_less_than(self):
		below_1000 = {
			"is_limit" : True,
			"less than" : True,
			"value" : 1000
		}

		self.set_test_vals("<1000")

		self.assertEqual(below_1000, self.query_vals)

if __name__=="__main__":
	unittest.main()