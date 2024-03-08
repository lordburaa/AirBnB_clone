#!/usr/bin/python3 
"""
test user
"""
from models.base_modelimport BaseModel
from models.user import User
from models.engine import file_storage

FileStorage = file_storage.FileStorage
class TestUser(unnittest.TestCase):
    """user Test """

    @classmethod
    def setUpClass():
        obj = User()

    def test_class(self):
        """test class """
        assert isinstance(type(obj), dict)

if __name__ == "__main__":
    unnitest.main()
