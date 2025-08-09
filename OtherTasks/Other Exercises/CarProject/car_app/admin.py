from django.contrib import admin
from .models import Manufacturer, Car, Autoservice, ScheduledRepair


# Register your models here.
class ManufacturerInline(admin.TabularInline):
    model = Autoservice.specialized_manufacturers.through
    extra = 1
    verbose_name = "Collaborating Manufacturer"
    verbose_name_plural = "Collaborating Manufacturers"


# Admin class for AutoService with inlines and required functionalities
class AutoserviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_founded', 'services_oldtimers',)
    inlines = [ManufacturerInline]

    def save_model(self, request, obj, form, change):
        if not change or request.user.is_superuser:
            super().save_model(request, obj, form, change)

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        if obj is not None:
            return False
        return True


# Admin class for Manufacturer with the required functionalities
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name',)

    def has_add_permission(self, request):
        return request.user.is_superuser


# Admin class for Car
class CarAdmin(admin.ModelAdmin):
    list_display = ('car_type', 'max_speed',)


admin.site.register(Autoservice, AutoserviceAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(ScheduledRepair)
