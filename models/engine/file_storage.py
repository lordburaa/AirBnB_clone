#!/usr/bin/python3
"""
clss FileStorage
"""
import json
import os
import copy


class FileStorage:
    """File Storage class is created"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """all method"""
        #self.__objects = json.dumps(self.__objects)
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as r:
                self.__objects = json.load(r)
        return self.__objects

    def new(self, obj):
        """new obj"""
        self.__objects={f"{obj.__class__.__name__}.{obj.id}": str(obj.to_dict())}
        

    def save(self):
        """save the file"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path) as r:
                r = json.load(r)
                self.__objects = {**r, **self.__objects}
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(self.__objects, f)


    def reload(self):
        """reload object from the file"""
    
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as r:
                self.__objects = json.load(r)
