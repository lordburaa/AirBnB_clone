import unittest

class TestUP(unittest.TestCase):
	def setUp(self):
		print("setUP")
		self.n = 5

	def tearDown(self):
		print("teardown")
		del self.n

	def test_new(self):
		print(self.n)

	@classmethod
	def setUpClass(cls):
		print("set up class")

	@classmethod
	def tearDownClass(cls):
		print("teardown class")
