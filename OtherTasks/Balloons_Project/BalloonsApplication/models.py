from django.contrib.auth.models import User
from django.db import models


# Create your models here.

# За секој балон се чуваат:
# - типот на балонот
# - име на производителот на балонот
# - максимален дозволен број на патници во балонот
class Balloon(models.Model):
    type = models.CharField(max_length=50)
    manufacturerName = models.CharField(max_length=50)
    maxNumOfPassengers = models.IntegerField()


# За секој пилот се чуваат:
# - име на пилот
# - презиме на пилот
# - година на раѓање на пилотот
# - вкупно часови на лет на пилотот
# - чин кој пилотот го има во компанијата
class Pilot(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    yearOfBirth = models.IntegerField()
    totalFlightHours = models.IntegerField()
    rank = models.CharField(max_length=50)


# За секоја авиокомпнија се чуваат:
# - име на авиокомпанија
# - година на основање на авиокомпанијата
# - информација дали лета надвор од Европа или не
class Airline(models.Model):
    name = models.CharField(max_length=50)
    yearOfEstablishment = models.IntegerField()
    fliesOutOfEurope = models.BooleanField()


# дополнително:
# - информација за пилотите со кои соработува (1:N) - еден пилот може да биде соработник на повеќе авиокомпании (1:M) = (N:M)
class AirlinePilot(models.Model):
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)


# За секој лет се чуваат:
# - задолжителна шифра на летот
# - име на кој аеродром полетува
# - име на кој аеродром слетува
# - корисник кој го креирал летот
# - фотографија за летот
# - информација со кој балон се изведува летот
# - пилот на летот
# - авиокомпанија која го реализира летот
class Flight(models.Model):
    # ID = models.AutoField(primary_key=True)
    code = models.CharField(max_length=50)
    nameOfAirportTakingOff = models.CharField(max_length=50)
    nameOfAirportLanding = models.CharField(max_length=50)
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='FlightImages/', null=True, blank=True)
    balloon = models.ForeignKey(Balloon, on_delete=models.CASCADE)
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
