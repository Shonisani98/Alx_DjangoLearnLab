from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
# Author model stores the name of each author.
# Each author can have multiple books (one-to-many relationship).

# Book model stores title, publication year, and links to an author.
# BookSerializer handles all fields and includes validation for publication_year.
# AuthorSerializer includes nested BookSerializer to show related books.
