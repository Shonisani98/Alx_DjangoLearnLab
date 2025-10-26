# Create
from bookshelf.models import Book
Book.objects.create(title="1984", author="George Orwell", publication_year=1949)


# Retrieve
from bookshelf.models import Book
Book.objects.get(title="1984")
# <Book: 1984 by George Orwell (1949)>


# Update
book.title = 'Nineteen Eighty-Four'
book.save()
# Output: Book updated: Book object (Nineteen Eighty-Four)

# Delete
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()
# Expected output: <QuerySet []>
