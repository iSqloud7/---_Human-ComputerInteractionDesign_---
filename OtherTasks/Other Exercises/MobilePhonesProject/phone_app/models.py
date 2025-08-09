from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Manufacturer(models.Model):
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    description=models.TextField()
    date=models.DateField()
    fromEU=models.BooleanField()
    def __str__(self):
        return self.name
class Phone(models.Model):
    PHONE_TYPE_CHOICE=[
        ("Small", "Small"),
        ("Medium", "Medium"),
        ("Large", "Large")
    ]
    manufacturer=models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    model=models.CharField(max_length=50)
    type=models.CharField(max_length=20, choices=PHONE_TYPE_CHOICE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='phone_images', null=True, blank=True)
    price=models.IntegerField()
    year=models.IntegerField()
    new_or_not=models.BooleanField()

    def __str__(self):
        return self.model