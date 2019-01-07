from django.shortcuts import render, get_object_or_404
from .models import Book, Author, BookNotes, BooksRead, Genre
from django.http import HttpResponse
from django.urls import reverse_lazy
from .forms import BookForm, AuthorForm, NotesForm, BookReadForm, GenreForm, FinishReadingForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    bookcount=Book.objects.all().count()
    authorcount=Author.objects.all().count()
    notecount=BookNotes.objects.all().count()
    readcount=BooksRead.objects.exclude(dateended__isnull=True).count()

    context={
        'bookcount': bookcount,
        'authorcount' : authorcount,
        'notecount' : notecount,
        'readcount' : readcount,
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
    return render (request, 'read/booksforauthor.html', {'book_list': book_list})
    #next add link in getauthors and a template

def getnotes(request):
    notes_list=BookNotes.objects.all()
    return render(request,'read/getnotes.html', {"notes_list" : notes_list})

def getbooksread(request):
    read_list=BooksRead.objects.all()
    return render(request, 'read/booksread.html', {'read_list' : read_list})

def getgenres(request):
    genre_list=Genre.objects.all()
    return render(request,'read/genres.html', {'genre_list' : genre_list})

def booksforgenre(request, id):
    book_list=Book.objects.filter(genre=id)
    return render(request, 'read/booksforgenre.html', {'book_list': book_list})

#Form views.
def addBook(request):
    form=BookForm

    if request.method=='POST':
        form=BookForm(request.POST)
        if form.is_valid():
            
            post=form.save(commit=True)
            post.save()
            form=BookForm()
    else:
        form=BookForm()
    return render(request, 'read/addbook.html', {'form': form})

def addAuthor(request):
    form=BookForm

    if request.method=='POST':
        form=AuthorForm(request.POST)
        if form.is_valid():
            
            post=form.save(commit=True)
            post.save()
            form=AuthorForm()
    else:
        form=AuthorForm()
    return render(request, 'read/addauthor.html', {'form': form})

def newNote(request):
    form=NotesForm

    if request.method=='POST':
        form=NotesForm(request.POST)
        if form.is_valid():
            
            post=form.save(commit=True)
            post.save()
            form=NotesForm()
    else:
        form=NotesForm()
    return render(request, 'read/newnote.html', {'form': form})

def addReading(request):
    form=BookReadForm

    if request.method=='POST':
        form=BookReadForm(request.POST)
        if form.is_valid():
            
            post=form.save(commit=True)
            post.save()
            form=BookReadForm()
    else:
        form=BookReadForm()
    return render(request, 'read/addbookread.html', {'form': form})

def addGenre(request):
    form=GenreForm

    if request.method=='POST':
        form=GenreForm(request.POST)
        if form.is_valid():
            
            post=form.save(commit=True)
            post.save()
            form=GenreForm()
    else:
        form=GenreForm()
    return render(request, 'read/addgenre.html', {'form': form})


def finishBook(request, pk):
    form=FinishReadingForm()
    book_instance = get_object_or_404(BooksRead, pk=pk)

  
    if request.method == 'POST':

        
        form = FinishReadingForm(request.POST)

       
        if form.is_valid():
            
            book_instance.dateended= form.cleaned_data['finish_date']
            book_instance.save()
            form=BookReadForm()
            
            #return HttpResponseRedirect(reverse('getbooksread') )

        else:
            form=FinishReadingForm()
    

    context = {
        'form': form,
        'book_instance': book_instance,
    }

    return render(request, 'read/finishbook.html', context)

#to do
#finish and when clicking on an author get books--done
#more measures of books read and by month and year
#add paging and other touches
#create forms for each model table--done
#spruce up the appearance some
#create test for the views models and forms
#add genres and from genres list books for that genre --done
#and then add links to the books from the genre list--done
#also maybe add thumbnail pictures of the books
#modify the css some