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
        old = self.__objects
        new ={f"{obj.__class__.__name__}.{obj.id}": obj.to_dict()}

        self.__objects = {**old, **new}

    def save(self):
        """save the file"""
        dic = self.__objects
        if os.path.exists(self.__file_path):
            with open(self.__file_path) as r:
                r = json.load(r)
                dict_t = {**r, **self.__objects}
                dic = dict_t
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(dic, f)


    def reload(self):
        """reload object from the file"""
    
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as r:
                self.__objects = json.load(r)
