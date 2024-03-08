#!/usr/bin/python3
"""
user Class

"""
from models.base_model import BaseModel


class User(BaseModel):
    """user Class created"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

