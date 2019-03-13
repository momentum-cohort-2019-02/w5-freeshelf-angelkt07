from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('bookcategories/', views.BookCategoryListView.as_view(), name='bookcategory'),
    path('bookcategory/<int:pk>', views.BookCategoryDetailView.as_view(), name='bookcategory-detail'),
]