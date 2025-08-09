from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Pilot(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    year_of_birth = models.IntegerField()
    flying_hours = models.IntegerField()
    act = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Balloon(models.Model):
    balloon_type = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50)
    max_passengers = models.IntegerField()

    def __str__(self):
        return f'{self.balloon_type}'


class Airline(models.Model):
    name = models.CharField(max_length=50)
    year_of_establishment = models.IntegerField()
    Flight_out_Europe = models.BooleanField()

    def __str__(self):
        return f'{self.name}'


class Flight(models.Model):
    code = models.CharField(max_length=50)
    start_airport_name = models.CharField(max_length=50)
    end_airport_name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flight_image = models.ImageField(upload_to='flight_images/', null=True, blank=True)
    balloon = models.ForeignKey(Balloon, on_delete=models.CASCADE)
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.code} {self.start_airport_name} {self.end_airport_name} {self.balloon} {self.pilot} {self.airline} '


class PilotAirline(models.Model):
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pilot.first_name} {self.pilot.last_name}"
