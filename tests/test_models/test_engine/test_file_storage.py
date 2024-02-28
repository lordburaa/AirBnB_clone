#!/usr/bin/python3
"""
contain the Test file storage docs classes
"""
from datetime import datetime
from models.engine import file_storage
from models.base_model import BaseMOdel
import json
import os
import unittest
FileStorage = file_storage.FileStorage

class TestFileStorage(unittest.TestCase):
    """ test The FileStorage class """
    def test_all_returns_dict(self):
        """test that all returns the FileStorage"""
        storage = FileStorage()
        new_dict = storage.all()
        self.assertEqual(type(new_dict), dict)
        self.assertIs(new_dict, storage._FileStorage__objects)
