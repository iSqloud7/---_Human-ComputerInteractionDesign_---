from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Flight
from .forms import FlightForm
# Create your views here.

def index(request):
    return render(request, 'index.html')
def flights(request):
    user_flights=Flight.objects.filter(user=request.user, start_airport_name="Skopje").all()
    if request.method == 'POST':
        form=FlightForm(request.POST, request.FILES)
        if form.is_valid():
           flight= form.save(commit=False)
           flight.user = request.user
           flight.flight_image=form.cleaned_data['flight_image']
           flight.save()

        return redirect('flights')
    else:
        form = FlightForm()
    return render(request, 'flights.html', {'flights': user_flights, 'form': form})