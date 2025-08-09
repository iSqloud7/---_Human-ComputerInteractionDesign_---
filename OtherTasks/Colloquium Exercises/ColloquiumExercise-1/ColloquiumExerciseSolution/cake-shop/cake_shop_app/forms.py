from django import forms

from cake_shop_app.models import Cake


class CakeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CakeForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = Cake
        exclude = ['baker']