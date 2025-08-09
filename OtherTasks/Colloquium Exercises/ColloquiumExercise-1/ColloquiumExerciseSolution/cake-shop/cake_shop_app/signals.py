from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
import random

from cake_shop_app.models import Baker, Cake


@receiver(pre_delete, sender=Baker)
def my_handler(sender, instance, **kwargs):
    cakes = Cake.objects.filter(baker=instance)

    other_bakers = Baker.objects.exclude(id=instance.id).all()

    for cake in cakes:
        new_baker = random.choice(other_bakers)
        cake.baker = new_baker
        cake.save()
