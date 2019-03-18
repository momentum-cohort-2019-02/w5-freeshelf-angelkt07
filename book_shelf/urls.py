from django.urls import path, include
from book_shelf import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('category/<int:pk>', views.CategoryDetailView.as_view(), name='category_detail'),
    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('book/create/', views.BookCreate.as_view(), name='book_create'),
    path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
    path('category/create/', views.CategoryCreate.as_view(), name='category_create'),
    path('book/<slug:slug>/update/', views.BookUpdate.as_view(), name='book_update'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
    path('category/<int:pk>/update/', views.CategoryUpdate.as_view(), name='category_update'),
    path('book/<slug:slug>/delete/', views.BookDelete.as_view(), name='book_delete'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
    path('category/<int:pk>/delete/', views.CategoryDelete.as_view(), name='category_delete'),
]