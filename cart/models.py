from django.db import models
from catalog.models import Book

# Create your models here
class History(models.Model):
    books = models.ManyToManyField(Book)

    def __str__(self):
        return ', '.join([book.title for book in self.books.all()])
