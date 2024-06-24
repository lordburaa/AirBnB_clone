#!/usr/bin/python3
"""
class of base
"""
import  uuid

from datetime import datetime
class BaseModel():
	""" base model test """
	def __init__(self, *args, **kwargs):
		if kwargs is not None:
			if 'id' not in kwargs:
				self.id = str(uuid.uuid4())
			for k in kwargs:
				if (k == '__class__'):
					pass
				else:
					setattr(self, k, kwargs[k])
		
		self.id = str(uuid.uuid4())
		self.created_at = datetime.now()
		self.updated_at = datetime.now()

	def __str__(self):
		print("the class printing \n {} \n".format(self.__dict__))
		return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

	def to_dict(self):
		dic_t = self.__dict__.copy()
		dic_t['__class__'] = self.__class__.__name__
		dic_t['created_at'] = self.created_at.isoformat()
		dic_t['updated_at'] = self.updated_at.isoformat()
		return dic_t

	def save(self):
		self.updated_at = datetime.now()
