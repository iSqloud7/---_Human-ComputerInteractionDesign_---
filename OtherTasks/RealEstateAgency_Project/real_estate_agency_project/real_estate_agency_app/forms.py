from django.forms import forms

from real_estate_agency_app.models import RealEstate


# class RealEstateForm(forms.ModelForm):
#     class Meta:
#         model = RealEstate
#         fields = '__all__'

class RealEstateForm(forms.ModelForm):
    class Meta:
        model = RealEstate
        fields = [
            'name', 'location_description', 'area', 'photo', 'is_reserved', 'is_sold', 'agents', 'features', 'price'
        ]
        widgets = {
            'agents': forms.CheckBoxSelectMultiple,
            'features': forms.CheckBoxSelectMultiple
        }
