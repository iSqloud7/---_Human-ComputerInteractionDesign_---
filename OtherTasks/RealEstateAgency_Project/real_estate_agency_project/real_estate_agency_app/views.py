from datetime import date
from msilib.schema import Property

from django.shortcuts import render, get_object_or_404, redirect

from real_estate_agency_app.forms import RealEstateForm
from real_estate_agency_app.models import RealEstate


# Create your views here.

def index(request):
    properties = Property.objects.all()

    if request.user.is_superuser:
        properties = properties.filter(published_date=date.today()).all()
    else:
        properties = properties.filter(agent__user=request.user).all()

    return render(request, "index.html", {"properties": properties})


def add_property(request, id):
    form = RealEstateForm()

    if request.method == 'POST':
        form = RealEstateForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return index
        else:
            form = RealEstateForm()
            return render(request, 'add_property.html', {'form': form})


def edit_property(request, pk):
    property_obj = get_object_or_404(RealEstate, pk=pk)

    if request.method == 'POST':
        form = RealEstateForm(request.POST, request.FILES, instance=property_obj)

        if form.is_valid():
            updated_property = form.save(commit=False)
            total_price = 0

            for feature in form.cleaned_data['features']:
                total_price += feature.price

            updated_property.price = total_price
            updated_property.save()
            form.save()

            return redirect('index')
    else:
        form = RealEstateForm(instance=property_obj)

    return render(request, 'edit_property.html', {
        'form': form,
        'property_obj': property_obj
    })
