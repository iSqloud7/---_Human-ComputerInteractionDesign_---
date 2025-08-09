from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# Секој маркет се карактеризира со
# име,
# работен персонал, (посебен модел)
# производи, (посебен модел)
# контакт информации, (посебен модел)
# број на маркети,
# датум на отварање,
# корисник којшто го додал,
# работно време од и
# работно време до.
class Market(models.Model):
    name = models.CharField(max_length=50)
    opening_date = models.DateField(null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    working_hours_from = models.TimeField(null=True, blank=True)
    working_hours_to = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


# За секој вработен се чува:
# - име,
# - презиме,
# - ЕМБГ,
# - корисник кој што го додал,
# - неговата плата.
# Еден вработен може да работи во само еден маркет.
class Employee(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    uniqueID = models.CharField(max_length=15, unique=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    market = models.ForeignKey(Market, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} --- {self.surname} --- {self.uniqueID} --- {self.salary} --- {self.market}"


# За контакт информациите се чува:
# - улицата и
# - бројот на којшто се наоѓа маркетот,
# - телефонскиот број и
# - емаил адресата.
class ContactInfo(models.Model):
    street = models.CharField(max_length=50)
    street_number = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    email_address = models.CharField(max_length=50)
    market = models.ForeignKey(Market, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.street} --- {self.street_number} --- {self.phone_number} --- {self.email_address} --- {self.market}"


# За еден производ се чува:
# - неговото име,
# - вид (храна, пијалок, пекара, козметика, хигиена),
# - дали производот е домашен и
# - неговиот код.
class Product(models.Model):
    SPECIES_CHOICES = [
        ('food', 'Food'),
        ('beverage', 'Beverage'),
        ('bakery', 'Bakery'),
        ('cosmetics', 'Cosmetics'),
        ('hygiene', 'Hygiene')
    ]
    name = models.CharField(max_length=50)
    species = models.CharField(max_length=50, choices=SPECIES_CHOICES)
    is_homemade = models.BooleanField(default=False)
    code = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.name}"


# - Секој маркет продава повеќе производи.
# - За производите се знае во кои маркети се достапни како и
# - достапната количина во секој од маркетите.
class ProductMarket(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"Product: {self.product} ----- Market: {self.market} ----- Quantity: {self.quantity}"
