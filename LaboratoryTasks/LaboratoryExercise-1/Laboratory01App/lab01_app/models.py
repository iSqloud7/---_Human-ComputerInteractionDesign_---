from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Ocena(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dzvezdi = {
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
    }
    broj_dzvezdi = models.CharField(max_length=50, choices=dzvezdi)
    komentar = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user} - {self.broj_dzvezdi}"


class Turist(models.Model):
    ime = models.CharField(max_length=50)
    prezime = models.CharField(max_length=50)
    datum_ragjanje = models.DateField(null=True, blank=True)
    broj_pasos = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.ime} - {self.prezime} - {self.broj_pasos}"


class KontaktInfo(models.Model):
    adresa = models.CharField(max_length=50)
    tel_broj = models.CharField(max_length=50)
    mejl_adresa = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.adresa} - {self.tel_broj} - {self.mejl_adresa}"


class TuristickiPaket(models.Model):
    ime = models.CharField(max_length=50)
    opis = models.CharField(max_length=50)
    destinacija = models.CharField(max_length=50)
    vremetraenje_denovi = models.IntegerField()
    cena = models.DecimalField(decimal_places=2, max_digits=10)
    datum_poagjanje = models.DateField(null=True, blank=True)
    broj_slobodni_mesta = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # turist = models.ForeignKey(Turist, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.ime} - {self.destinacija} - {self.datum_poagjanje}"
        # return f"{self.ime} - {self.opis} - {self.destinacija} - {self.cena} - {self.datum_poagjanje} - {self.user} - {self.turist}"


class Agencija(models.Model):
    ime = models.CharField(max_length=50)
    sopstvenik = models.CharField(max_length=50)
    kontakt_info = models.ForeignKey(KontaktInfo, on_delete=models.CASCADE)
    datum_osnovanje = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    turisticki_paketi = models.ForeignKey(TuristickiPaket, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.ime}"
        # return f"{self.ime} - {self.sopstvenik} - {self.kontakt_info} - {self.datum_osnovanje} - {self.user} - {self.turisticki_paketi}"


class TuristickiPaketTurist(models.Model):
    turisticki_paket = models.ForeignKey(TuristickiPaket, on_delete=models.CASCADE)
    turist = models.ForeignKey(Turist, on_delete=models.CASCADE)
    datum = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.turisticki_paket} - {self.turist} - {self.datum}"


class TuristickiPaketOcena(models.Model):
    turisticki_paket = models.ForeignKey(TuristickiPaket, on_delete=models.CASCADE)
    ocena = models.ForeignKey(Ocena, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.turisticki_paket} - {self.ocena}"
