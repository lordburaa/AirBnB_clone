#!/usr/bin/python3
"""
user class
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    user base class is created
    """
    def __init__(self):
        """ initalization """
        self.email = ''
        self.password = ''
        self.first_name = ''
        self.last_name = ''
        super().__init__()

