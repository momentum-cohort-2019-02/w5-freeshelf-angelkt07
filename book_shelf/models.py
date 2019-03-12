from django.db import models, IntegrityError
from django.urls import reverse
from django.core.validators import URLValidator
import uuid

# Create your models here.

class BookShelf(models.Models):
    """ Model to set up the basics of the book shelf. """
    pass

class Book(models.Models):
    """ Model to set up the basics of each book"""
    title = models.CharField(max_length=100)
    author = models.ForeignKey('BookAuthor', on_delete=models.SET_NULL, null=True)
    bookcategory = models.ManyToManyField('BookTopic', help_text='This is the language or main topic of the book.')
    book_description = models.TextField(max_length=500)
    book_url = models.TextField(validators=[URLValidator()], max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=30)

    class Meta:
        ordering = [-created_at]

    def __str__(self):
        """string for title of book"""
        return self.title

    def display_bookcategory(self):
        """ Create a string for the category name"""
        return ', '.join(bookcategory.name for bookcategory in self.bookcategory.all()[:3])

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
    pass

class BookURL(models.Model):
