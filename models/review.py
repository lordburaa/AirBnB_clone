#!/usr/bin/python3
"""review """
from models.base_model import BaseModel
from models.place import Place
from models.user import User

class Review(BaseModel):
    """Review Model """
    palace_id = Place.id
    user_id = User.id
    text = ''

