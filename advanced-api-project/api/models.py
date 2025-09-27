from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
# Author model stores the name of each author.
# Each author can have multiple books (one-to-many relationship).

# Book model stores title, publication year, and links to an author.
# BookSerializer handles all fields and includes validation for publication_year.
# AuthorSerializer includes nested BookSerializer to show related books.
