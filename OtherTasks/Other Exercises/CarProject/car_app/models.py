from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Manufacturer(models.Model):
    name = models.CharField(max_length=50)
    website = models.URLField()
    country = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Car(models.Model):
    car_type = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    max_speed = models.FloatField()
    color = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.car_type}"


class Autoservice(models.Model):
    name = models.CharField(max_length=50)
    year_founded = models.IntegerField()
    services_oldtimers = models.BooleanField()
    specialized_manufacturers = models.ManyToManyField(Manufacturer, related_name='specialized_services')

    def __str__(self):
        return self.name


class ScheduledRepair(models.Model):
    code = models.CharField(max_length=50)
    registered_date = models.DateField()
    problem_desc = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    problem_image = models.ImageField(upload_to='cars_images/', blank=True, null=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    auto_service = models.ForeignKey(Autoservice, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.code}"
