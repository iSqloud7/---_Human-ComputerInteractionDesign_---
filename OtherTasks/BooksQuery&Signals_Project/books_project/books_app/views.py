from django.shortcuts import render
from books_app.models import Book
from django.db.models import Q, Avg


# Create your views here.

def book_list(request):
    # books = Book.objects.all()

    # books = Book.objects.filter(title = "The Silent Grove")

    # book = Book.objects.get(title = "The Silent Grove")
    # books = [book]

    # books = Book.objects.filter(publisher_year__gte=2007)
    # books = Book.objects.filter(publisher_year__lte=2007)

    # books = Book.objects.filter(Q(publisher_year__gte=2007) | Q(title__icontains="Past"))
    # books = Book.objects.filter(Q(publisher_year__lte=2015) & Q(title__icontains="Grove"))

    # books = Book.objects.filter(author__name="Ivan")

    # num_of_books = Book.objects.all().count()
    # books = Book.objects.order_by("publisher_year") # ASC
    # books = Book.objects.order_by("-publisher_year") # DESC

    # num_of_books = Book.objects.all().count()
    # books = Book.objects.order_by("publisher_year")[1:2]

    num_of_books = Book.objects.all().count()
    books = Book.objects.order_by("publisher_year")[:]
    avg_of_books = Book.objects.aggregate(average_year=Avg("publisher_year"))

    return render(request, 'book_list.html', {'books': books, 'total_books': num_of_books, 'avg_books': avg_of_books})
