#!/usr/bin/python3
""" city class  """

from models.base_model import BaseModel
from models.state import State


class City(BaseModel):
    """city class """
    state_id = ''
    name = ''
