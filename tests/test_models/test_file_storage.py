#!/usr/bin/python3
"""
unnittest
"""
class TestFileStorage(unittest.TestCase):
    """Test File Storag """

    @classmethod
    def setUpClass():
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()
    
    def test_all(self):
        """Testing the all method """
        assert isinstance(type(my_dict), dict)

if __name__ == '__main__':
    unittest.main()
