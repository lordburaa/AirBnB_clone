#!/usr/bin/python3
""" unittes for models engine
"""
import os
import json
from models.base_model import BaseModel
import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """ unittest for the file storage """

    def test_file_storage_instance(self):
        self.assertEqual(FileStorage, type(FileStorage))
