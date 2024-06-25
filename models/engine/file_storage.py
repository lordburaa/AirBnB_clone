#!/usr/bin/python3
""" file storage class """
import json
import os
import datetime
from models.base_model import BaseModel


class FileStorage:
    """ storage for the file """
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """initialization doc """
        pass

    def all(self):
        """ returing all method """
        return self.__objects

    def new(self, obj):
        """ returning new func"""

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ save file json format"""
        obj_dict = {}
        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """ reload json file """
        if (os.path.exists(self.__file_path)):
            with open("file.json") as f:
                self.__objects = json.load(f)

        else:
            return
