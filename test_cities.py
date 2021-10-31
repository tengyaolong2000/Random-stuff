import unittest
from employees import Employee

class EmployeeTestCase(unittest.TestCase):

	def setUp(self):
		self.teng = Employee('Teng', 'Yao Long', 50000000)
		

	def test_give_default_raise(self):
		self.teng.give_raise()
		self.assertEqual(self.teng.annual_salary, 50005000)

	def test_give_custom_raise(self):
		self.teng.give_raise(10000000)
		self.assertEqual(self.teng.annual_salary, 60000000)
unittest.main()
