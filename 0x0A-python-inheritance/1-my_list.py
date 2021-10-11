#!/usr/bin/python3
"""
Inherit Module
"""


class MyList(list):
	"""
	MyList class that inherits from List
	"""
	def print_sorted(self):
		"""
		prints a sorted list
		"""
		print(sorted(self))