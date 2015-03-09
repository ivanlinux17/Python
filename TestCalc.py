from Calc import Calc
import unittest

class TestCal (unittest.TestCase):
	def setUp(self):
		self.calc = Calc ()

	def test_00_sum (self):
		self.assertEqual(self.calc.sum(2,2),4)
		
if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(TestCal)
	unittest.TextTestRunner(verbosity=2).run(suite)