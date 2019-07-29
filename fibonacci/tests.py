from django.test import TestCase
from .views import get_number

# Create your tests here.

class number_to_test(TestCase):
	def test_get_number_view(self):
		response = self.client.get('/fibonacci/number/10')
		self.assertEqual(response.status_code, 301)