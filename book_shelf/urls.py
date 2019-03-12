from django.urls import path
from book_shelf.models import BookShelf, Book, BookCategory, BookAuthor
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]