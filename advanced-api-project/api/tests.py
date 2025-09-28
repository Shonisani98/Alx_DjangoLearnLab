from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.author = Author.objects.create(name='J.R.R. Tolkien')
        self.book = Book.objects.create(title='The Hobbit', publication_year=1937, author=self.author)

    def test_list_books(self):
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('The Hobbit', str(response.data))

    def test_create_book_authenticated(self):
        self.client.force_authenticate(user=self.user)
        data = {
            'title': 'The Silmarillion',
            'publication_year': 1977,
            'author': self.author.id
        }
        response = self.client.post('/books/create/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'The Silmarillion')

    def test_create_book_unauthenticated(self):
        data = {
            'title': 'The Silmarillion',
            'publication_year': 1977,
            'author': self.author.id
        }
        response = self.client.post('/books/create/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book(self):
        self.client.force_authenticate(user=self.user)
        data = {'title': 'The Hobbit: Revised'}
        response = self.client.put(f'/books/{self.book.id}/update/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'The Hobbit: Revised')

    def test_delete_book(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(f'/books/{self.book.id}/delete/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_filter_books_by_title(self):
        response = self.client.get('/books/?title=The Hobbit')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books(self):
        response = self.client.get('/books/?search=Hobbit')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('The Hobbit', str(response.data))

    def test_order_books_by_year(self):
        Book.objects.create(title='The Silmarillion', publication_year=1977, author=self.author)
        response = self.client.get('/books/?ordering=publication_year')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'The Hobbit')

