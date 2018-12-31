from django import forms
from .models import Book, Author, BookNotes, BooksRead, Genre

class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields='__all__'

class AuthorForm(forms.ModelForm):
    class Meta:
        model=Author
        fields='__all__'

class NotesForm(forms.ModelForm):
    class Meta:
        model=BookNotes
        fields='__all__'

class BookReadForm(forms.ModelForm):
    class Meta:
        model=BooksRead
        fields='__all__'

class GenreForm(forms.ModelForm):
    class Meta:
        model=Genre
        fields='__all__'