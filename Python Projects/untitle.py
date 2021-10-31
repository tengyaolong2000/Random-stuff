import requests
import unittest

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)

def get_status_code():
	return r.status_code




class StatusTestCase(unittest.TestCase):

	def test_status_code(self):
		status_code = get_status_code()
		self.assertEqual(status_code, 200)


unittest.main()