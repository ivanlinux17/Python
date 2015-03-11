from Calc import Calc
from xmlrunner.unittest import unittest
import xmlrunner

class TestCal (unittest.TestCase):
	def setUp(self):
		self.calc = Calc ()

	def test_00_sum (self):
		print "Hello world"
		self.assertEqual(self.calc.sum(2,2),4)

	def test_01_sum2 (self):
		print "This test should fail"
		self.assertEqual(self.calc.sum(2,3),6)

	def test_02_sub (self):
		print "2 minus 2 = %d" %self.calc.sub(2,2)
		self.assertEqual(self.calc.sub(2,2),0)
		
if __name__ == '__main__':
	#suite = unittest.TestLoader().loadTestsFromTestCase(TestCal)
	#unittest.TextTestRunner(verbosity=2).run(suite)

	unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports', verbosity=3))