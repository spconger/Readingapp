from django.shortcuts import render, get_object_or_404
from .models import Book, Author, BookNotes, BooksRead
from django.http import HttpResponse
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    bookcount=Book.objects.all().count()
    authorcount=Author.objects.all().count()
    notecount=BookNotes.objects.all().count()

    context={
        'bookcount': bookcount,
        'authorcount' : authorcount,
        'notecount' : notecount,
    }
    return render(request, 'read/index.html', context=context)

def getbooks (request):
    book_list=Book.objects.all()
    return render(request, 'read/getbooks.html', {'book_list' : book_list })

def bookdetail(request, id):
    book=get_object_or_404(Book, pk=id)
    return render(request, 'read/bookdetail.html', {'book' : book})


def getauthors(request):
    author_list=Author.objects.all()
    return render(request,'read/getauthors.html', {'author_list' : author_list})

def booksforauthor(request, id):
    book_list=Book.objects.filter(author=id)
    return render (request, 'read/booksforauthor.htnml', {'book_list': book_list})
    #next add link in getauthors and a template

def getnotes(request):
    notes_list=BookNotes.objects.all()
    return render(request,'read/getnotes.html', {"notes_list" : notes_list})

def getbooksread(request):
    read_list=BooksRead.objects.all()
    return render(request, 'read/booksread.html', {'read_list' : read_list})


#to do
#finish and when clicking on an author get books
#more measures of books read and by month and year
#add paging and other touches
#create forms for each model table
#spruce up the appearance some
#create test for the views models and forms