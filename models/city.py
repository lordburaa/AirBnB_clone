#!/usr/bin/python3
"""
add city class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """add city clas
    """
    state_id = ""
    name = ""

    def __init__(self):
        super().__init__()
