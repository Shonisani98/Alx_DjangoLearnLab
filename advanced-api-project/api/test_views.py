from rest_framework.test import APITestCase, APIClient
from rest_framework import status


class DummyTest(TestCase):
    def test_dummy(self):
        self.assertEqual(1, 1)
class BookAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        # rest of your setup...
self.assertEqual(response.status_code, status.HTTP_200_OK)
self.assertIn('The Hobbit', str(response.data))
