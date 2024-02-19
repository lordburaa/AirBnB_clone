#!/usr/bin/python3
"""
Base mode 

"""
import date



class BaseModel:
    """base Model class creaed"""
    def __init__(self, id=None):
        self.id = str(uuid.uuid4())
        self.created_at = date
        self.updated_at = chage 

    def __str__(self):
        return f"{self.__class__.__name__} ({self.id}) {self.__dict__}"

    def created_at(self, *args):
        pass

    @classmethod
    def updated_at(cls):
        pass

    def save(self):
        self.updated_at =


    def to_dict(self):

        return self.__dict__

