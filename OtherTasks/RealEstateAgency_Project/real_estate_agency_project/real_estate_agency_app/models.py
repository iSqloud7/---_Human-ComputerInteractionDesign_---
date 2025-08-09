from django.contrib.auth.models import User
from django.contrib.gis.gdal.feature import Feature
from django.db import models
from torch.testing._internal.distributed.rpc.examples.reinforcement_learning_rpc_test import Agent


# Имате задача да креирате систем за управување со агенција за недвижности.
# Системот треба интуитивно да ги прикажува недвижностите кои се продаваат, (НЕДВИЖНОСТИ)
# да нуди информации за агентите кои се задолжени за продажба и (АГЕНТИ ЗА ПРОДАЖБА)
# да овозможува лесно пребарување на недвижностите според карактеристиките кои ги имаат. (КАРАКТЕРИСТИКИ)

# Create your models here.

# Секоја недвижност која може да се огласи за продавање се карактеризира со:
# - име,
# - опис на локацијата каде се наоѓа,
# - површина која ја зафаќа,
# - датум кога е објавена за продавање,
# - фотографија,
# - информација дали некој ја резервирал и
# - информација дали е веќе можеби продадена.

class RealEstate(models.Model):
    name = models.CharField(max_length=50)
    location_description = models.TextField()
    area = models.PositiveIntegerField()
    published_date = models.DateField(auto_now_add=True)
    photo = models.ImageField(upload_to='real_estate_photos/')
    is_reserved = models.BooleanField(default=False)
    is_sold = models.BooleanField(default=False)
    # Еден агент може да биде одговорен за повеќе недвижности, а една недвижност може да ја нудат повеќе агенти.
    # Агентите задолжени за одредена недвижност лесно се додаваат во Админ панелот во делот за недвижност.
    agents = models.ManyToManyField(Agent, blank=True)
    # Карактеристиките за една недвижност исто така се додаваат во делот за недвижности.
    features = models.ManyToManyField(Feature, blank=True)
    # Недвижноста нема почетна цена,
    # туку таа се креира како сума од вредностите на карактеристиките кои таа недвижност ги поседува.
    price = models.IntegerField(default=0)

    def calculate_price(self):
        return sum(feature.price for feature in self.features.all())

    def __str__(self):
        return self.name


# Агентите кои се задолжени за продажба во агенцијата се карактеризираат со:
# - име и
# - презиме,
# - телефон за контакт,
# - линк до нивен профил од LinkedIn,
# - број на извршени продажби до сега и
# - email адреса.

class Agent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=50)
    linked_in_link = models.URLField(max_length=50);
    total_sales = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.first_name} - {self.user.last_name}"


# На пример, доколку недвижнота располага со лифт, тогаш во цената се додава $10000,
# поседувањето на базен е $25000 итн (цените ги одредувате Вие при креирање на карактеристиките).

class Feature(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name
