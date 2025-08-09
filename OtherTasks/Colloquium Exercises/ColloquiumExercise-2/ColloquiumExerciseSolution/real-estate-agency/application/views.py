from django.shortcuts import render

from application.forms import RealEstateForm
from application.models import RealEstate, CharacteristicRealEstate


# Create your views here.
def index(request):
    houses = RealEstate.objects.filter(sold=False, area__gte=100).all()
    real_estate_context = []
    for house in houses:
        price = 0
        house_characteristics = CharacteristicRealEstate.objects.filter(real_estate=house)
        for house_characteristic in house_characteristics:
            price += house_characteristic.characteristic.value
        real_estate_context.append({'house': house, 'price': price})

    return render(request, 'index.html', {'houses': real_estate_context})

def edit(request, house_id):
    instance = RealEstate.objects.filter(id=house_id).first()
    if request.method == 'POST':
        form = RealEstateForm(request.POST, files=request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return index(request)
    form = RealEstateForm(instance=instance)
    return render(request, 'details.html', {'form': form, 'house': instance})