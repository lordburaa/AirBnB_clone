#!/usr/bin/python3
"""
class created
"""
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """Test the BaseModel class"""
    def test_str(self):
        """test that str method has the correct output"""
        inst = BaseModel()
        string = "[BaseModel] ({}) {}".format(inst.id, inst.__dict__)
        self.assertEqual(string, str(inst))
