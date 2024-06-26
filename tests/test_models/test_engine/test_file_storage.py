#!/usr/bin/python3
import unittest
from  models.engine.file_storage import FileStorage



class TestFileStorage(unittest.TestCase):
    """ unittest for the file storage """
    
    def test_instance(self):
        f = FileStorage()
        self.assertEqual(FileStorage,type(FileStorage)))
