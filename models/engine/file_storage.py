#!/usr/bin/python3
"""
clss FileStorage
"""
import json
import os
import models


class FileStorage:
    """File Storage class is created"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """all method"""
        # self.__objects = json.dumps(self.__objects)
        # if os.path.exists(self.__file_path):
        return FileStorage.__objects

    def new(self, obj):
        """creating new key if not exist"""
        key = f"{obj.__class__.__name__}.{obj.id}"

        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """save the file"""
        json_obj = FileStorage.__objects.copy()
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump({key: value for key, value in FileStorage.__objects.items()}, f)

    def reload(self):
        """reload object from the file"""
        try:

            with open(FileStorage.__file_path, "r", encoding="utf-8") as r:
                obj_dict = json.load(r)
                FileStorage.__objects = obj_dict
        except FileNotFoundError:
            pass
