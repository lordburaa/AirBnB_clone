import os 
import sys
import unittest
from console import Mycmd

class TestMycmd(unittest.TestCase):

    def test_prompt_string(self):
        self.assertEqual("hbnb) ". Mycmd.prompt)
