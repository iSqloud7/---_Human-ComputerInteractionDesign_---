from django.shortcuts import render

from PublishingBooks.models import Book


# Create your views here.

def books(request):
    context = {"books": Book.objects.all()}
    # context = {"books": Book.objects.all(), "date" : "07.07.2003"}
    # context = {"books": Book.objects.filter(title='Book')}
    # context = {"books": Book.objects.filter(author__first_name="Ivan")}
    return render(request, "books.html")
