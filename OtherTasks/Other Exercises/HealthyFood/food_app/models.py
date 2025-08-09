from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()
    active=models.BooleanField()
    def __str__(self):
        return self.name

class Product(models.Model):
    code=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    description=models.TextField()
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    image=models.ImageField(upload_to='product_images/', null=True, blank=True)
    price=models.IntegerField()
    quantity=models.IntegerField()
    def __str__(self):
        return self.name

class Client(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    email=models.EmailField(null=True, blank=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Sale(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.IntegerField()
    date=models.DateField()
    client=models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product} {self.quantity} {self.client}"