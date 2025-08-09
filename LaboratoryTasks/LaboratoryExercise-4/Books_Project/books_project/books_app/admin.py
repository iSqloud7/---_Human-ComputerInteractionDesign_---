from django.contrib import admin

from books_app.models import Kniga, IzdavackaKukja


# Register your models here.

class KnigaAdmin(admin.ModelAdmin):
    list_display = (
        "naslov", "slika", "isbn", "god_izdavanje", "izdavacka_kukja", "broj_strani", "broj_strani", "tip_korica",
        "tip_kategorija", "cena",)


admin.site.register(Kniga, KnigaAdmin)


class IzdavackaKukjaAdmin(admin.ModelAdmin):
    list_display = (
        "ime", "zemja", "grad", "god_osnovanje", "vebsajt",)


admin.site.register(IzdavackaKukja, IzdavackaKukjaAdmin)
