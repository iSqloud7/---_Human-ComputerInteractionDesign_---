from django.db.models.signals import post_save
from django.dispatch import receiver

from real_estate_agency_app.models import RealEstate


# Кога еден оглас/недвижнина ќе се означи како продадена,
# потребно е сите агенти поврзани со неа да ја инкрементираат својата продажба.
@receiver(post_save, sender=RealEstate)
def increase_sales_count_on_sold(sender, instance, **kwargs):
    if instance.is_sold:
        for agent in instance.agents.all():
            agent.total_sales += 1
            agent.save()