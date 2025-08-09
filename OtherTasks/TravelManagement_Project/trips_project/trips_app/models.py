from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class CustomUser(AbstractUser):
    contact = models.CharField(max_length=50)
    is_guide = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Trip(models.Model):
    destination = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.DurationField()
    picture = models.ImageField(upload_to='trip_pictures/')
    creator = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.creator} - {self.destination} - {self.price}$"
