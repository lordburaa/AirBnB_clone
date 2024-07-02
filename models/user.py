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
        email = ""
        password = ""
        first_name = ""
        last_name = ""
