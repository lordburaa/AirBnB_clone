#!/usr/bin/python3
"""
clss FileStorage
"""
import json
import models
import os

class FileStorage:
    """File Storage class is created"""
    __file_path = "file.json"
    __objects = {}


    def all(self):
        """all method"""
        # self.__objects = json.dumps(self.__objects)
        # if os.path.exists(self.__file_path):
        return self.__objects

    def new(self, obj):
        """creating new key if not exist"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key]= obj
    
    def save(self):
        """save the file"""
        obj_dict = {}
        
        for key in FileStorage.__objects:
            print("main",self.__objects[key].to_dict())
            obj_dict[key] = self.__objects[key].to_dict()
        
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """reload object from the file"""
        if os.path.exists(FileStorage.__file_path):
            with open(self.__file_path, 'r', encoding="utf-8") as r:
                self.__objects = json.load(r)
