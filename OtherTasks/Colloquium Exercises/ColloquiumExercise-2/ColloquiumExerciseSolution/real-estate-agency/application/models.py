from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class RealEstate(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    area = models.DecimalField(decimal_places=2, max_digits=10)
    image = models.ImageField(upload_to='real_estates/')
    date = models.DateField()
    characteristic = models.CharField(max_length=255, default="", null=True, blank=True) #used for showing the chars per house on the edit form
    reserved = models.BooleanField(default=False)
    sold = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Agent(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    profile_url = models.URLField()
    contact_phone = models.CharField(max_length=50)
    total_sales = models.IntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class AgentRealEstate(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    real_estate = models.ForeignKey(RealEstate, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.agent.name} {self.real_estate.name}"

class Characteristic(models.Model):
    name = models.CharField(max_length=100)
    value = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.name

class CharacteristicRealEstate(models.Model):
    characteristic = models.ForeignKey(Characteristic, on_delete=models.CASCADE)
    real_estate = models.ForeignKey(RealEstate, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.characteristic.name} {self.real_estate.name}"
