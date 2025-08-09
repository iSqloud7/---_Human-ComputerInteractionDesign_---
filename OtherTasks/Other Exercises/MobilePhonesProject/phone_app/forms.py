from django import forms
from .models import Phone

class PhoneForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PhoneForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model= Phone
        fields = "__all__"
        exclude = ['user']
