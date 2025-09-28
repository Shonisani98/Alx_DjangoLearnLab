from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from .models import Author, Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create test user and log in
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

        # Create test author and book
        self.author = Author.objects.create(name='J.R.R. Tolkien')
        self.book = Book.objects.create(
            title='The Hobbit',
            publication_year=1937,
            author=self.author
        )

    # Example test using response.data and status
    def test_list_books(self):
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('The Hobbit', str(response.data))
