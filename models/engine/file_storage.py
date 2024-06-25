#!/usr/bin/python3
""" file storage class """
import json
import os



class FileStorage:
    """ storage for the file """
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        pass

    def all(self):
        """ returing all method """
        return self.__objects

    def new(self, obj):
        """ returning new func"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj.__str__()

    def save(self):
        """ save file json format"""
        r = {}
        tmp = {}
        if os.path.exists(self.__file_path):
            with open("file.json") as t:
                r = json.load(t)
        tmp = {**r, **self.__objects}
        with open(self.__file_path, 'w') as f:
            json.dump(tmp, f)

    def reload(self):
        """ reload json file """
        if (os.path.exists(self.__file_path)):
            with open("file.json") as f:
                self.__objects = json.load(f)
