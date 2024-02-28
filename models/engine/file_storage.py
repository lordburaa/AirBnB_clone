#!/usr/bin/python3
"""
clss FileStorage
"""
import json
import models


class FileStorage:
    """File Storage class is created"""
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        pass

    def all(self):
        """all method"""
        # self.__objects = json.dumps(self.__objects)
        # if os.path.exists(self.__file_path):
        return self.__objects

    def new(self, obj):
        """creating new key if not exist"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key]= obj.to_dict()

    def save(self):
        """save the file"""
        json_obj = {}
        for key in self.__objects:
            json_obj[key] = self.__objects[key]
            print("test")
        with open(self.__file_path, "w", encoding="utf-8") as f:
            f.write(json.dumps(json_obj))

    def reload(self):
        """reload object from the file"""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as r:
            #jo = json.load(r)
                self.__objects = json.load(r)
        except:
            pass
