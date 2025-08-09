from django.contrib import admin
from BalloonsApplication.models import Pilot, Balloon, Airline, Flight, AirlinePilot


# Register your models here.

class PilotAdmin(admin.ModelAdmin):
    # 4.За пилотите и авиокомпаниите во листата се прикажуваат само нивните имиња и презиме на пилотот.
    list_display = ("name", "surname",)


admin.site.register(Pilot, PilotAdmin)


class BalloonAdmin(admin.ModelAdmin):
    list_display = ("type", "manufacturerName", "maxNumOfPassengers",)


admin.site.register(Balloon, BalloonAdmin)


class FlightAdmin(admin.ModelAdmin):
    # 1.При креирање на летот, корисникот се доделува автоматски според најавениот корисник.
    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)

    # 2.Откако еден лет ќе биде креиран и зачуван, истиот може да се промени само од корисникот кој го креирал летот.
    def has_change_permission(self, request, obj=None):
        if obj and request.user == obj.created_by:
            return True
        return False

    # 3.Не е дозволено бришење на летовите за ниту еден корисник.
    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Flight, FlightAdmin)


class AirlinePilotInline(admin.StackedInline):  # StackedInline -> класата нема да се појави во Админ панелот
    model = AirlinePilot


class AirlineAdmin(admin.ModelAdmin):
    # Потребно е да се овозможи додавање на објекти преку Админ панелот,
    # со забелешка дека пилотите-соработници на една авиокомпанија се додаваат во делот за авиокомпанија.
    inlines = [AirlinePilotInline, ]
    # 4.За пилотите и авиокомпаниите во листата се прикажуваат само нивните имиња и презиме на пилотот.
    list_display = ("name",)


admin.site.register(Airline, AirlineAdmin)
