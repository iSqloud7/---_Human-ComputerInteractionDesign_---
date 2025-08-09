from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Cake(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='cakes/', null=True, blank=True)
    baker = models.ForeignKey('Baker', on_delete=models.CASCADE, null=True, blank=True, related_name='cakes')

    def __str__(self):
        return self.name


class Baker(models.Model):
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='bakers/', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"