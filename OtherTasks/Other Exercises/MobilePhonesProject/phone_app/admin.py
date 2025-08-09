from django.contrib import admin
from .models import Manufacturer, Phone
# Register your models here.
class PhoneAdmin(admin.ModelAdmin):
    exclude = ('user',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(PhoneAdmin, self).save_model(request,obj,form,change)

admin.site.register(Phone,PhoneAdmin)
admin.site.register(Manufacturer)