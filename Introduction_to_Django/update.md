from bookshelf.models import Book

book = Book.objects.get(title='1984')
book.title = 'Nineteen Eighty-Four'
book.save()

# ✏️ Updated book: Nineteen Eighty-Four George Orwell 1949

