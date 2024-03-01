#!/usr/bin/python3
"""
Module for the Base Class
-public instnace attributes
    -id
    -created_at
    -updated_at

-Public instnace methods
    -save(self) - updates the updated_at attribute
    -to_dict(self) - returns dictionary

"""
from datetime import datetime
import uuid
from models import storage
# from .engine.file_storage import FileStorage


class BaseModel:
    """base Model class creaed"""
    def __init__(self, *args, **kwargs):
        """instianation"""
        if kwargs:
            self.__dict__ = kwargs.copy()
            #for key, value in kwargs.items():
            #    setattr(self, key, value)
            if "created_at" not in self.__dict__:
                setattr(self, "created_at", datetime.now())
            if "updated_at" not in self.__dict__:
                setattr(self, "updated_at", datetime.now())
        else:

            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            #old
            #self.updated_at = self.created_at
            #new
            self.updated_at = datetime.now()
            storage.new(self)
            storage.save()

    def __str__(self):
        """str representation"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """save the time"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """to dictionary"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = type(self).__name__
        new_dict["created_at"] = self.updated_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()

        #Include Dynamicaly declared attributes

        return new_dict
