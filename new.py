#!/usr/bin/python3


class Base():
	def __init__(self):
		self.id = 12
		self.name = "bura"

		print(dict(self.__dict__))
		self.f = 'datgim'
c= Base()
