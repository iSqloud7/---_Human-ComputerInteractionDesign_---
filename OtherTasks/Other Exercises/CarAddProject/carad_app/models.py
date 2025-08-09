from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Manufacturer(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    year_of_establishment = models.IntegerField()
    number_of_employees = models.IntegerField()

    def __str__(self):
        return self.name


class Car(models.Model):
    CAR_TYPE_CHOICE = [
        ("SEDAN", "SEDAN"),
        ("SUV", "SUV"),
        ("HATCHBACK", "HATCHBACK"),
        ("COUPE", "COUPE")
    ]
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    price = models.IntegerField()
    chassis_number = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    year_of_production = models.IntegerField()
    km = models.IntegerField()
    type = models.CharField(max_length=20, choices=CAR_TYPE_CHOICE)
    image = models.ImageField(upload_to='cars_images', null=True, blank=True)

    def __str__(self):
        return self.model
