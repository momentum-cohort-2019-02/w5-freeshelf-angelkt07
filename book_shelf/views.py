import datetime
from django.shortcuts import render
from book_shelf.models import Book, Category, Author
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

def index(request):
    """Index view"""
    books = Book.objects.all()
    num_book = Book.objects.all().count()
    num_category = Category.objects.all().count()
    num_author = Author.objects.all().count()

    context = {
        'books' : books,
        'num_book' : num_book,
        'num_category' : num_category,
        'num_author' : num_author,
    }

    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book
    paginate_by = 10

class BookDetailView(generic.DetailView):
    model = Book
    
class CategoryListView(generic.ListView):
    model = Category
    paginate_by = 10

class CategoryDetailView(generic.DetailView):
    model = Category

class AuthorListView(generic.ListView):
    model = Author


