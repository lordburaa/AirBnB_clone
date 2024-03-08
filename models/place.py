#!/usr/bin/python3
"""
adding user class
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """adding place """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    # type int
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self):
        super().__init__()
