from django.contrib import admin
from .models import Oglas, Category
# Register your models here.

class OglasAdmin(admin.ModelAdmin):
    exclude = ['user',]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(OglasAdmin, self).save_model(request, obj, form, change)


admin.site.register(Oglas, OglasAdmin)
admin.site.register(Category)