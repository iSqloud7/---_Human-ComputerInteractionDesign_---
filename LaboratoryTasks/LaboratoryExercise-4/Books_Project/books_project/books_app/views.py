from django.shortcuts import render

from books_app.models import Kniga


# Create your views here.

def index(request):
    knigi = Kniga.objects.all()

    return render(request, 'index.html', {"knigi": knigi})


def details(request, kniga_id):
    kniga = Kniga.objects.filter(id=kniga_id).first()
    context = {'flight_data': kniga, 'app_name': 'books_app'}
    return render(request, 'details.html', context)
