#!/usr/bin/python3
"""
Base mode

"""
from datetime import datetime
import uuid


class BaseModel:
    """base Model class creaed"""
    def __init__(self, *args, **kwargs):
        """inistantiatio"""
        self.id = str(uuid.uuid4())
        self.created_at = str(datetime.now().isoformat('-'))
        self.updated_at = str(datetime.now().isoformat('-'))

    def __str__(self):
        """str representation"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    @staticmethod
    def updated_at():
        """updated at"""
        self.updated_at = str(datetime.now().isoformat('-'))

    def save(self):
        """save the time"""
        self.updated = str(datetime.now().isoformat('-'))

    def to_dict(self):
        """to dictionary"""
        self.__dict__["__class__"] = "BaseModel"
        return self.__dict__
