import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import permission_required, login_required
from django.urls import reverse, reverse_lazy
from django.views.decorators.http import require_http_methods


from book_shelf.models import Book, Category, Author

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

class AuthorDetailView(generic.DetailView):
    model = Author

class BookCreate(CreateView):
    model = Book
    fields = ('title', 'author', 'category', 'summary', 'book_url', 'picture')

class AuthorCreate(CreateView):
    model = Author
    fields = '__all__'
    success_url = reverse_lazy('authors')

class CategoryCreate(CreateView):
    model = Category
    fields = '__all__'
    success_url = reverse_lazy('categories')

class BookUpdate(UpdateView):
    model = Book
    fields = ('title', 'author', 'category', 'summary', 'book_url', 'picture')

class AuthorUpdate(UpdateView):
    model = Author
    fields = '__all__'

class CategoryUpdate(UpdateView):
    model = Category
    fields = '__all__'

class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('index')

class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('authors')

class CategoryDelete(DeleteView):
    model = Category
    success_url = reverse_lazy('categories')


# def favorite_book_view(request, book_pk):
#     book = get_object_or_404(Book, pk=book_pk)

#     favorite, created = request.user.favorite_set.get_or_create(book=book)

#     if created:
#         return
#     else:
#         favorite.delete()

#     return redirect(book.get_absolute_url())






