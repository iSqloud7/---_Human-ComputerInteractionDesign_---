from django import forms
from .models import Oglas

class OglasForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(OglasForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Oglas
        exclude=['user']
