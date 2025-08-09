from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class IzdavackaKukja(models.Model):
    ime = models.CharField(max_length=50)
    zemja = models.CharField(max_length=50)
    grad = models.CharField(max_length=50)
    god_osnovanje = models.DateField()
    vebsajt = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.ime} {self.zemja} {self.grad} {self.god_osnovanje} {self.vebsajt}"

class Kniga(models.Model):
    KORICI_CHOICES = [
        ("M", "Meka"),
        ("T", "Tvrda")
    ]
    KATEGORII_CHOICES = [
        ("R", "Romansa"),
        ("T", "Triler"),
        ("B", "Biografija"),
        ("K", "Klasik"),
        ("D", "Drama"),
        ("I", "Istorija")
    ]
    naslov = models.CharField(max_length=50)
    slika = models.ImageField(upload_to="sliki", null=True, blank=True)
    isbn = models.CharField(max_length=50)
    god_izdavanje = models.DateField()
    izdavacka_kukja = models.ForeignKey(IzdavackaKukja, on_delete=models.CASCADE)
    broj_strani = models.IntegerField()
    dimenzii = models.IntegerField()
    tip_korica = models.CharField(max_length=50, choices=KORICI_CHOICES)
    tip_kategorija = models.CharField(max_length=50, choices=KATEGORII_CHOICES)
    cena = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.naslov} {self.slika} {self.isbn} {self.god_izdavanje} {self.izdavacka_kukja} {self.broj_strani} {self.dimenzii} {self.izdavacka_kukja} {self.tip_korica} {self.tip_kategorija} {self.cena} "
