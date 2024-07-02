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
    email = ""
    password = ""
    first_name = ""
    last_name = ""
