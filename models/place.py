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
    number_rooms = 3
    number_bathrooms = 4
    max_guest = 4
    price_by_night = 3
    latitude = 0.0
    longitude = 4.0
    amenity_ids = []
