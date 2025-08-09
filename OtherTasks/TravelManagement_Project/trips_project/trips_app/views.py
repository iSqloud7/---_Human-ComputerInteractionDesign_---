from django.shortcuts import render

from trips_app.models import Trip


# Create your views here.

def index(request):
    trips = Trip.objects.all()

    return render(request, 'index.html', {'trips': trips})
