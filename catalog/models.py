from django.db import models
from django.urls import reverse
import uuid

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=200, help_text="Enter a book genre")

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=200, help_text="Enter the language of the book")

    def __str__(self):
        return self.name

class Book(models.Model):
    call_no = models.CharField('Call number', max_length=200, blank=True, help_text="Enter the classification number of the book")
    title = models.CharField(max_length=200)
    series = models.CharField(max_length=200, blank=True)
    author = models.ManyToManyField('Author', help_text="Select author for the book")
    genre = models.ManyToManyField(Genre, help_text="Select genre(s) for the book")
    desc = models.TextField(max_length=2000, blank=True, default="No description available.", help_text="Enter a brief description of the book")
    isbn_13 = models.CharField('ISBN-13', primary_key=True, max_length=13, help_text="Enter ISBN of the book")
    img_url_s = models.URLField('Image URL (small)', default='/static/img/default.png', help_text="Enter the URL to book cover image (small)")
    img_url_m = models.URLField('Image URL (medium)', default='/static/img/default.png', help_text="Enter the URL to book cover image (medium)")
    img_url_l = models.URLField('Image URL (large)', default='/static/img/default.png', help_text="Enter the URL to book cover image (large)")

    class Meta:
        ordering = ['title']
        
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.isbn_13)])

    def display_author(self):
        return '\n'.join([' '.join([author.first_name, author.last_name]) for author in self.author.all()[:3]])
    display_author.short_description = 'Author'

    def display_author_inline(self):
        return ', '.join([' '.join([author.first_name, author.last_name]) for author in self.author.all()[:3]])
        display_author_inline.short_description = 'Author'

    def display_genre(self):
        return '\n'.join([genre.name for genre in self.genre.all()[:3]])
    display_genre.short_description = 'Genre'

class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular book across whole library. Do not modify.")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    location = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True)

    LOAN_STATUS = (
        ('a', 'Available'),
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text="Book availability")

    class Meta:
        ordering = ['due_back']
            
    def __str__(self):
        return '{0} ({1})'.format(self.id, self.book.title)

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    desc = models.TextField(max_length=2000, blank=True, help_text="Enter a brief description of the author")

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])
    
    def __str__(self):
        return '{0}, {1}'.format(self.last_name, self.first_name)

class Location(models.Model):
    x_coor = models.FloatField()
    y_coor = models.FloatField()

    class Meta:
        ordering = ['x_coor', 'y_coor']

    def __str__(self):
        return '{0}, {1}'.format(self.x_coor, self.y_coor)
