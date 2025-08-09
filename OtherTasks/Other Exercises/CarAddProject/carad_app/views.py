from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CarAddForm
from .models import Car
# Create your views here.

def index(request):
    car=Car.objects.all()
    context={"cars":car, "form":CarAddForm}
    return render(request, "index.html", context)

def detail(request, car_id):
    car=get_object_or_404(Car, pk=car_id)
    return render(request, "detail.html", {"car":car})
def create(request):
    if request.method=="POST":
        form_data=CarAddForm(data=request.POST, files=request.FILES)
        if form_data.is_valid():
            car=form_data.save(commit=False)
            car.image=form_data.cleaned_data['image']
            car.save()

            return HttpResponseRedirect("/")

    return render(request, "create.html", context={"form":CarAddForm})

def delete(request, car_id):
    car_instance=Car.objects.filter(id=car_id).get()
    if request.method=="POST":
        car_instance.delete()
        return redirect("/")
    return render(request, "delete.html")

def edit(request, car_id):
    car_instance=Car.objects.filter(id=car_id).get()
    if request.method=="POST":
        car=CarAddForm(request.POST, instance=car_instance)
        if car.is_valid():
            car.save()
        return redirect("/")
    else:
        car=CarAddForm(instance=car_instance)
    return render(request, "edit.html", {"form":car})