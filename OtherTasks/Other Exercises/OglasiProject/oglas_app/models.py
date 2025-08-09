from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    category_description=models.TextField()
    date=models.DateField()
    realeastate=models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Oglas(models.Model):
    STATUS_CHOICE=[
        ('ФИКСНА','Цената е фиксна'),
        ('ПРЕДЛОЗИ', 'Прифаќам предлози'),
        ('НЕ ФИКСНА', "Цената не е фиксна")
    ]
    title=models.CharField(max_length=200)
    description=models.TextField()
    time=models.TimeField()
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='oglas_images/', blank=True, null=True)
    price=models.IntegerField()
    status=models.CharField(max_length=50, choices= STATUS_CHOICE)
    new_user=models.BooleanField(default=True)
    def __str__(self):
       return self.title
