#!/usr/bin/python3
""" file storage class """
import json
import os



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
        r = {}
        tmp = {}
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding="utf-8") as t:
                r = json.load(t)
        for key, value in self.__objects.items():
            tmp[key] = value.__str__()
        r = {**r, **tmp}

        with open(self.__file_path, 'w') as f:
            json.dump(r, f)

    def reload(self):
        """ reload json file """
        if (os.path.exists(self.__file_path)):
            with open("file.json") as f:
                self.__objects = json.load(f)
        else:
            return
