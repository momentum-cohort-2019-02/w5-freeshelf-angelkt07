import datetime

from django.shortcuts import render
from book_shelf.models import Book, BookCategory
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

    num_book = Book.objects.all().count()
    num_categories = BookCategory.objects().count()

    context = {
        'num_book' : num_book,
        'num_categories' : num_categories,
    }

    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book
    paginate_by = 10

class BookDetailView(generic.DetailView):
    model = Book
    
class BookCategoryListView(generic.ListView):
    model = BookCategory
    paginate_by = 10

class BookCategoryDetailView(generic.DetailView):
    model = BookCategory

