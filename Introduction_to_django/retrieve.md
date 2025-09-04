from bookshelf.models import Book

book = Book.objects.get(title='The Pragmatic Programmer')
print("📘 Retrieved book:", book)
