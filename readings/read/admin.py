from django.contrib import admin
from .models import Author, Genre, Book, BooksRead, BookNotes



# Register your models here.
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(BooksRead)
admin.site.register(BookNotes)
