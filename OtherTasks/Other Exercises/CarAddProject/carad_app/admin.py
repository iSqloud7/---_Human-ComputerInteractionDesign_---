from django.contrib import admin
from .models import Manufacturer, Car
# Register your models here.

class ManufacturerAdmin(admin.ModelAdmin):
    # exclude=("user",)
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(ManufacturerAdmin, self).save_model(request,obj,form,change)

admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Car)