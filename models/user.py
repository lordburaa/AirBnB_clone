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
        self.email = ''
        self.password = ''
        self.first_name = ''
        self.last_name = ''
        if kwargs:
            super().__init__(**kwargs)
        else:
            super().__init__()
