from django.contrib import admin
from .models import Balloon, Pilot, PilotAirline, Airline, Flight
# Register your models here.
class PilotAirlineInlineAdmin(admin.TabularInline):
    model = PilotAirline
    extra = 0
    list_display = ('pilot.first_name')

class AirlineAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [PilotAirlineInlineAdmin]

class FlightAdmin(admin.ModelAdmin):
    list_display = ('code', 'start_airport_name', 'end_airport_name', 'balloon', 'pilot', 'airline',)
    exclude = ['user',]
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class PilotAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name',)

admin.site.register(Balloon)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Airline, AirlineAdmin)
admin.site.register(Pilot, PilotAdmin)
