from bookshelf.models import Book

book = Book(
    title='The Pragmatic Programmer',
    author='Andrew Hunt',
    publication_year=1999
)
book.save()

print("✅ Book created:", book)
