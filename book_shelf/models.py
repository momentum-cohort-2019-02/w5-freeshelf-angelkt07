from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse

# Create your models here.

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

    class Meta:
        ordering = ['-date_added']

    def display_category(self):
        return ', '.join(category.name for category in self.category.all()[:3])

    def __str__(self):
        """ string to return self.title"""
        return self.title

    def get_absolute_url(self):
        """Returns the URL to access a detail record for the book"""
        return reverse('book-detail', args=[str(self.id)])

class Category(models.Model):
    """Book Categories"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Author(models.Model): 
    """Book Author"""
    author = models.CharField(max_length=255)

    def __str__(self):
        return self.author



    
