from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Book(models.Model):
    """Class for my book model"""
    title = models.CharField(max_length=255)
    author = models.ForeignKey('Author', null=True, blank=True, on_delete=models.SET_NULL)
    category = models.ManyToManyField('Category')
    summary = models.TextField(max_length=1000)
    book_url = models.URLField(unique=True)
    slug = AutoSlugField(populate_from='title', unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to='book_shelf/', null=True, blank=True)

    favorited_by = models.ManyToManyField(
        to=User, related_name='favorite_books', through='Favorite'
    )

    class Meta:
        ordering = ['-date_added']
        permissions = (
            ("Can_add_book", "Can add a book"),
            ("Can_change_book", "Can edit a book"),
            ("Can_delete_book", "Can delete a book"),
        )

    def display_category(self):
        return ', '.join(category.category for category in self.category.all()[:3])

    display_category.short_description = 'Category'

    def __str__(self):
        """ string to return self.title"""
        return self.title

    def get_absolute_url(self):
        """Returns the URL to access a detail record for the book"""
        return reverse('book-detail', args=[str(self.id)])

class Category(models.Model):
    """Book Categories"""
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category

class Author(models.Model): 
    """Book Author"""
    author = models.CharField(max_length=255)

    def __str__(self):
        return self.author

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    favorited_at = models.DateTimeField(auto_now_add=True)

    
