from bookshelf.models import Book

book = Book.objects.get(title='The Pragmatic Programmer')
book.publication_year = 2000
book.save()

print("✏️ Updated book:", book)
