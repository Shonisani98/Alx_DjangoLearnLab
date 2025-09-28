from rest_framework.test import APITestCase, APIClient


class DummyTest(TestCase):
    def test_dummy(self):
        self.assertEqual(1, 1)
class BookAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        # rest of your setup...
