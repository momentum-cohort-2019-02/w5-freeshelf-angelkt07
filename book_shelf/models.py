from django.db import models, IntegrityError
from django.urls import reverse
from django.core.validators import URLValidator
from autoslug import AutoSlugField
import uuid

# Create your models here.

class BookShelf(models.Model):
    """ Model to set up the basics of the book shelf. """
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Book(models.Model):
    """ Model to set up the basics of each book"""
    title = models.CharField(max_length=100)
    author = models.ForeignKey('BookAuthor', on_delete=models.SET_NULL, null=True)
    bookcategory = models.ManyToManyField('BookCategory', help_text='This is the language or main category of the book.')
    book_description = models.TextField(max_length=500)
    book_url = models.TextField(validators=[URLValidator()], max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from=['title'])

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        """string for title of book"""
        return self.title

    def display_bookcategory(self):
        """ Create a string for the category name"""
        return ', '.join(bookcategory.category for bookcategory in self.bookcategory.all()[:3])

    def get_absolute_url(self):
        """Returns the URL for the detail of the Book"""
        return reverse('book-detail', args=[str(self.id)])

    

class BookCategory(models.Model):
    """ Model for each topic of book so I can display certain kinds."""
    category = models.CharField(max_length=100)

    def __str__(self):
        """Return a string for the category"""
        return self.category

class BookAuthor(models.Model):
    """ Model for each Author"""
    author = models.CharField(max_length=35)
    category = models.ManyToManyField(BookCategory)

    def __str__(self):
        return author.author

