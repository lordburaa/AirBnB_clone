#!/usr/bin/python3
"""
class of base
"""
import uuid
from datetime import datetime


class BaseModel:
    """ base model test """

    def __init__(self, *args, **kwargs):
        """ init function """

        if len(kwargs) != 0:
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            for key, value in kwargs.items():
                if (key == '__class__'):
                    continue
                if (key == 'created_at'):
                    setattr(self, key, datetime.now())
                if (key == 'updated_at'):
                    setattr(self, key, datetime.now())
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """ str function """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        """ to dicct function """
        dic_t = self.__dict__.copy()
        dic_t['__class__'] = self.__class__.__name__
        dic_t['created_at'] = self.created_at.isoformat()
        dic_t['updated_at'] = self.updated_at.isoformat()
        return dic_t

    def save(self):
        """ save documentation a"""
        self.updated_at = datetime.now()
