from django.contrib import admin
from book_shelf.models import Book, Category, Author

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'summary', 'book_url', 'picture', 'slug')
  

admin.site.register(Category)
admin.site.register(Author)
