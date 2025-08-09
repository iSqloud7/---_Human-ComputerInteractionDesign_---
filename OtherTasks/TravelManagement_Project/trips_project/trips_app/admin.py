from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db.models import Count

from trips_app.models import CustomUser, Trip


# Register your models here.

class TripInline(admin.StackedInline):
    model = Trip
    extra = 1


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'is_guide',)
    inlines = [TripInline]
    fieldsets = UserAdmin.fieldsets + (
        ('Extra Info', {'fields': ('contact', 'is_guide',)}),
    )

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(trips_count=Count('trip')).filter(trips_count__lt=3)

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False


admin.site.register(CustomUser, CustomUserAdmin)


class TripAdmin(admin.ModelAdmin):
    exclude = ['creator',]
    list_display = ('destination', 'price', 'duration', 'picture',)

    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        obj.save()

    def has_add_permission(self, request):
        if request.user.is_guide:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if obj and obj.creator == request.user and request.user.is_guide:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if obj and obj.creator == request.user and request.user.is_guide:
            return True
        return False


admin.site.register(Trip, TripAdmin)
