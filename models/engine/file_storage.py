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
        key = "{}.{}".format(type(obj), obj.id)
        self.__objects[key] = obj

    def save(self):
        """ save file json format"""
        r = {}
        tmp = {}
        do = {}
        if os.path.exists(self.__file_path):
            with open("file.json") as t:
                r = json.load(t)
        for key, value in self.__objects.items():
            tmp[key] = value.__str__()
        do = {**tmp, **r}

        with open(self.__file_path, 'w') as f:
            json.dump(do, f)

    def reload(self):
        """ reload json file """
        if (os.path.exists(self.__file_path)):
            with open("file.json") as f:
                self.__objects = json.load(f)
