from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index' ),
   path('getbooks/', views.getbooks, name='getbooks'),
   path('getauthors/', views.getauthors, name='getauthors'),
   path('getnotes/', views.getnotes, name='getnotes'),
   path('getbooksread/', views.getbooksread, name='booksread'),
   path('bookdetail/<int:id>', views.bookdetail, name='bookdetail'),
   path('booksforauthor/<int:id>', views.booksforauthor, name='booksforauthor'),
   path('addBook/', views.addBook, name='addbook'),
   path('addAuthor/', views.addAuthor, name='addauthor'),
   path('newNotes/', views.newNote, name='newnote'),
   path('addGenre/', views.addGenre, name='addgenre'),
   path('addReading/', views.addReading, name='addreading'),
   path('finishBook/<int:pk>', views.finishBook, name='finishbook'),
   path('getgenres/', views.getgenres, name='genres'),
   path ('booksforgenre/<int:id>', views.booksforgenre, name='booksforgenre'),
   
]