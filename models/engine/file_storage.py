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
        try:
            with open(self.__file_path, "r", encoding="utf-8") as r:
                self.__objects = {**self.__objects, **json.load(r)}
        except FileNotFoundError as e:
            pass
        return self.__objects

    def new(self, obj):
        """new obj"""
        key = f"{obj.__class__.__name__}.{obj.id}"

        self.__objects[key] = obj.to_dict()

    def save(self):
        """save the file"""
        json_obj = self.__objects.copy()
        try:

            with open(self.__file_path, "r") as r:
                re = json.load(r)
                json_obj = {**re, **json_obj}
        except FileNotFoundError:
            pass
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(json_obj, f)

    def reload(self):
        """reload object from the file"""
        try:

            with open(self.__file_path, "r", encoding="utf-8") as r:
                self.__objects = json.load(r)
        except FileNotFoundError:
            pass
