from django import forms

from car_app.models import ScheduledRepair


class SheduledRepairForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(SheduledRepairForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = ScheduledRepair
        exclude = ("user",)
