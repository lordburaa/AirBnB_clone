#!/usr/bin/python3
"""
user class
"""

from models.base_model import BaseModel
from models import storage

class User(BaseModel):
    """
    user base class is created
    """
    def __init__(self, *args, **kwargs):
        """ initalization """
        super().__init__()
        self.email = ''
        self.password = ''
        self.first_name = ''
        self.last_name = ''
        self.__dict__['__class__'] = 'User'
      

    def __str__(self):
        """ str function """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
