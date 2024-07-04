#!/usr/bin/python3
""" file storage class """
import json
import os
import datetime


class FileStorage:
    """ storage for the file """
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """ initialization """
        pass

    def all(self):
        """ returing all method """
        return self.__objects

    def new(self, obj):
        """ returning new func"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ save file json format"""
        obj_dict = {}
        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def cls(self, key, **dicct):
        """ instance of the class """
        from models.base_model import BaseModel
        from models.user import User
        from models.city import City
        from models.place import Place
        from models.state import State
        from models.review import Review
        
        dic = {'BaseModel': BaseModel, 'User': User,
                'City': City, 'Place': Place,
                'State': State, 'review': Review}
        r = dic[key]
        return r(**dicct)

    def reload(self):
        """ reload json file """
        obj = None
        if (os.path.exists(FileStorage.__file_path)):
            with open(FileStorage.__file_path, 'r', encoding="UTF-8") as f:
                try:

                    obj = json.load(f)

                    for key, value in obj.items():
                        base = value['__class__']
                        FileStorage.__objects[key] = self.cls(base, **value)
                except FileNotFoundError:
                    pass
