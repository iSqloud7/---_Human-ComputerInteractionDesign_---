from django.contrib import admin

from lab01_app.models import Ocena, Turist, KontaktInfo, TuristickiPaket, Agencija, TuristickiPaketTurist, \
    TuristickiPaketOcena


# Register your models here.

class OcenaAdmin(admin.ModelAdmin):
    list_display = ('user', 'broj_dzvezdi')

    def has_change_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False


admin.site.register(Ocena, OcenaAdmin)


class KontaktInfoAdmin(admin.ModelAdmin):
    list_display = ('adresa', 'tel_broj', 'mejl_adresa')

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False


admin.site.register(KontaktInfo, KontaktInfoAdmin)


class TuristAdminInline(admin.TabularInline):
    model = TuristickiPaketTurist
    extra = 0
    list_display = ('ime', 'prezime', 'broj_pasos')

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(TuristAdminInline, self).save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False


admin.site.register(TuristickiPaketTurist)


class TuristickiPaketAdmin(admin.ModelAdmin):
    inlines = [TuristAdminInline]
    list_display = ('ime', 'destinacija', 'datum_poagjanje')
    list_filter = ('destinacija', 'cena')

    def has_change_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False


admin.site.register(TuristickiPaket, TuristickiPaketAdmin)
admin.site.register(Turist)


class AgencijaAdmin(admin.ModelAdmin):
    list_display = ('ime',)


admin.site.register(Agencija, AgencijaAdmin)


class TuristickiPaketOcenaAdmin(admin.ModelAdmin):
    list_display = ('turisticki_paket', 'ocena')


admin.site.register(TuristickiPaketOcena, TuristickiPaketOcenaAdmin)
