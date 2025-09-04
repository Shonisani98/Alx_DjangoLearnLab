from bookshelf.models import Book

book = Book.objects.get(title='The Pragmatic Programmer')
book.delete()

print("🗑️ Book deleted.")
