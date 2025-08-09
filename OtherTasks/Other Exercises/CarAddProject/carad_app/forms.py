from django import forms
from .models import Car

class CarAddForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CarAddForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model=Car
        fields="__all__"