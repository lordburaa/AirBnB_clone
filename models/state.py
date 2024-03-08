#!/usr/bin/python3
"""
state class
"""
from models.base_model import BaseModel


class State(BaseModel):
    name = ""
    
    def __init__(self):
        super().__init__()
