from django.shortcuts import render, get_object_or_404
from .models import Book, Author, BookInstance, Genre, Location
from cart.models import History
from django.views import generic
from django.db.models import Q
from django.utils import timezone
from django.urls import reverse
from django.http import JsonResponse

# Create your views here.
def index(request):
    # Change to popular books later
    book_list = Book.objects.all()[:4]

    return render(
        request,
        'index.html',
        context={'book_list':book_list},
    )

class BookListView(generic.ListView):
    model = Book
    paginate_by = 10

    # if request.method == 'GET'
    def get(self, request):
        q = request.GET.get('q')
        if q:
            book_list = Book.objects.filter(title__icontains=q)
            title = 'Search Results'
        else:
            book_list = Book.objects.all()
            title = 'Book List'
        return render(
            request,
            'catalog/book_list.html',
            {'book_list':book_list, 'title':title},
        )

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10

    # if request.method == 'GET'
    def get(self, request):
        q = request.GET.get('q')
        if q:
            author_list = Author.objects.filter(Q(first_name__icontains=q) | Q(last_name__icontains=q))
        else:
            author_list = Author.objects.all()
        return render (
            request,
            'catalog/author_list.html',
            {'author_list':author_list, 'title':'Author List'},
        )
    
class AuthorDetailView(generic.DetailView):
    model = Author
