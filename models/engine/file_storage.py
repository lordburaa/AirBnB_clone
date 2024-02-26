#!/usr/bin/python3
"""
clss FileStorage
"""
import json
import os
#from models.base_model import BaseModel
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
        if obj is not None:

            self.__objects={f"{obj.__class__.__name__}.{obj.id}": obj.to_dict()}
        

    def save(self):
        """save the file"""
        json_obj = self.__objects
        try:

            with open(self.__file_path, "r") as r:
                re = json.load(r)
                ob_dump = dumps(self.__objects)
                json_obj = {**re, **ob_dump}
        except:
            pass
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(json_obj, f)


    def reload(self):
        """reload object from the file"""
        try:

            with open(self.__file_path, "r", encoding="utf-8") as r:
                jo = json.load(r)
                self.__objects = jo
        except:
            pass

