from django.db import models

# Create your models here.
class Genre (models.Model):
    genrename = models.CharField(max_length=255)

    def __str__(self):
        return self.genrename
    
    class Meta:
        db_table='genre'

class Author(models.Model):
    authorname=models.CharField(max_length=255)

    def __str__(self):
        return self.authorname
    
    class Meta:
        db_table='author'


        
class Book (models.Model):
    title = models.CharField(max_length=255)
    author = models.ManyToManyField(Author)
    genre=models.ManyToManyField(Genre)
    pages=models.IntegerField(null=True, blank=True)
    description=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table='book'


class BooksRead(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    datestarted = models.DateField()
    dateended = models.DateField(null=True, blank=True)
    reread=models.CharField(max_length=3)
    quitdate=models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.datestarted)
    
    class Meta:
        db_table='booksread'

class BookNotes(models.Model):
    notetitle=models.CharField(max_length=255)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    notedate=models.DateField()
    notetext=models.TextField()

    def __str__(self):
        return self.notetitle

    class Meta:
        db_table='booknotes'