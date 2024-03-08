#!/usr/bin/python3
"""
clss FileStorage
"""
import json
import os

class FileStorage:
    """File Storage class is created"""
    __file_path = "file.json"
    __objects = {}


    def all(self):
        """all method"""
        # self.__objects = json.dumps(self.__objects)
        # if os.path.exists(self.__file_path):
        return FileStorage.__objects

    def new(self, obj):
        """creating new key if not exist"""
        name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(name, obj.id)] = obj
    
    def save(self):
        """save the file"""

        with open(self.__file_path, 'w', encoding="utf-8") as f:
            obj_dict = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(obj_dict, f)

    def classes(self):
        
        from models.base_model import BaseModel
        from models.user import User
        from models.amenity import Amenity
        classes = {"BaseModel": BaseModel,
                    "User": User,
                    "Amenity": Amenity
                }

        return classes

    def reload(self):
        """reload object from the file"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding="utf-8") as r:
                jo = json.load(r)
                jo = {k: self.classes()[v["__class__"]](**v) for k, v in jo.items()}
                FileStorage.__objects = jo
