#!/usr/bin/python3
"""
Base mode

"""
from datetime import datetime, time
import uuid

class BaseModel:
    """base Model class creaed"""
    def __init__(self, *args, **kwargs):
        """inistantiatio"""
        self.created_at = datetime.now()
        self.id = str(uuid.uuid4())
        self.updated_at = self.created_at

    def __str__(self):
        """str representation"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """save the time"""
        self.updated_at = datetime.now()
        
    def to_dict(self):
        """to dictionary"""
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["updated_at"] = self.updated_at
        sort_t = dict(sorted(new_dict.items(), reverse=True))
        return sort_t
