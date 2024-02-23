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
        if os.path.exists(self.__file_path):
            with open("file.json", "r") as r:
                self.__objects = json.load(r)
        return self.__objects

    def new(self, obj):
        """new obj"""
        self.__objects ={f"{obj.__class__.__name__}.{obj.id}": str(obj)}

    def save(self):
        """save the file"""
        dic = self.__objects
        if os.path.exists(self.__file_path):
            with open("file.json") as r:
                r = json.load(r)
                dict_t = {**r, **self.__objects}
                dic = dict_t
        with open("file.json", "w", encoding="utf-8") as f:
            json.dump(dic, f)


    def reload(self):
        """self"""
    
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as r:
                self.__objects = json.load(r)
