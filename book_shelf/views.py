from django.shortcuts import render

# Create your views here.

def index(request):
    """create a veiw for the index page."""

    num_book = Book.objects.all().count()
    num_category = BookCategory.objects.all().count()
    num_author = BookAuthor.ojbects.all().count()


    context = [
        'num_book' : num_book,
        'num_category' : num_category,
        'num_author' : num_author,
    ]

    return render(request, 'index.html', context=context)

