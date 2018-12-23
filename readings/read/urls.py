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
   
]