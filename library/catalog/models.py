from django.db import models
from django.urls import reverse
import uuid

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self) -> str:
        return f'Book genre {self.name}'


class Language(models.Model):
    lang = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f'{self.lang}'


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)  # If we delete the author, we just return the Author and not the book. Book author is set to NULL.
    summary = models.TextField(max_length=600)
    isbn = models.CharField('ISBN', max_length=13, unique=True)
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)
    # To connect book to multiple genre, we will establish many-to-many relationship
    # A book many belong to multiple Genre, hence many to many relation
    # A genre can have multiple book
    genre = models.ManyToManyField(Genre)

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.pk})
    
    # To access single record of the book, get_absolute_url is used
    def __str__(self) -> str:
        return f'Book {self.title} is authored by {self.author}'


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']
    
    def get_absolute_url(self):
        return reverse("author_detail", kwargs={"pk": self.pk})
    
    def __str__(self) -> str:
        return f'{self.last_name}, {self.first_name}'
    

class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    
    # If you have a book instance that is checked out, first you need to delete the book instance before you can delete the book
    book = models.ForeignKey('Book', on_delete=models.RESTRICT)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ("m", "Maintenance"),
        ("o", "On Loan"),
        ("a", "Available"),
        ("r", "Reserved")
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m')

    class Meta:
        ordering = ['due_back']
    
    def __str__(self) -> str:
        return f'{self.id} : ({self.book.title})'
