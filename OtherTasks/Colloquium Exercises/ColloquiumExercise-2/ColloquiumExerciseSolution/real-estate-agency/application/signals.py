from django.db.models import signals
from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch.dispatcher import receiver

from application.models import RealEstate, AgentRealEstate, CharacteristicRealEstate


@receiver(pre_save, sender=RealEstate)
def handle_saving_house(sender, instance, **kwargs):
    old_instance = sender.objects.filter(id=instance.id).first()
    if old_instance:
        if old_instance.sold != instance.sold:
            agents_real_estate = AgentRealEstate.objects.filter(real_estate=old_instance).all()
            for agent_real_estate in agents_real_estate:
                agent = agent_real_estate.agent
                agent.total_sales += 1
                agent.save()

@receiver([post_save, post_delete], sender=CharacteristicRealEstate)
def handle_saving_house(sender, instance, **kwargs):
    all_characteristics = sender.objects.filter(real_estate=instance.real_estate).all()
    if all_characteristics:
        real_estate = all_characteristics[0].real_estate
        real_estate.characteristic = ", ".join(char.characteristic.name for char in all_characteristics)
        real_estate.save()
