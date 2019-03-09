from django.test import TestCase
from .models import Book, BookNotes, BooksRead, Genre, Author

# Create your tests here.
#test models first:
class BookTest(TestCase):
    def test_stringOutput(self):
        book=Book(title='Django for Dummies')
        self.assertEqual(str(book), book.title)

class IndexTest(TestCase):
    
    def addbooks(self):
       Book.objects.create(title='Book1')
       Book.objects.create(title="Book2")
       Book.objects.create(title="Book3")

    def test_countbooks(self):
        
        bookcount=Book.objects.all().count()
        self.assertEqual(bookcount, 3)
