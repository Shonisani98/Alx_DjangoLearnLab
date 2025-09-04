# Create
from bookshelf.models import Book
book = Book(title='1984', author='George Orwell', publication_year=1949)
book.save()
# Output: Book created: Book object (1984)

# Retrieve
book = Book.objects.get(title='1984')
print(book.title, book.author, book.publication_year)
# Output: 1984 George Orwell 1949

# Update
book.title = 'Nineteen Eighty-Four'
book.save()
# Output: Book updated: Book object (Nineteen Eighty-Four)

# Delete
book.delete()
Book.objects.all()
# Output: []
