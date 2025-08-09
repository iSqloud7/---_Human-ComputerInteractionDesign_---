from django.forms import forms
from trips_app.models import *


class TripForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TripForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control'}

    class Meta:
        model = Trip
        fields = ['destination', 'price', 'duration', 'picture']
