from django.contrib import admin

from real_estate_agency_app.models import Agent, Feature, RealEstate
from datetime import date


# Register your models here.

# Во рамки на aдмин панелот потребно е да ги обезбедите следните функционалности:

class AgentAdmin(admin.ModelAdmin):
    # Агентите, Карактеристиките и Недвижностите се прикажани со нивното име (презиме, површина и опис ако ги имаат, соодветно).
    list_display = ('first_name', 'last_name',)

    # Агенти и Карактеристики може да бидат додадени само од супер-корисници.
    def has_add_permission(self, request):
        if (request.user.is_superuser):
            return True
        return False


admin.site.register(Agent, AgentAdmin)


class FeatureAdmin(admin.Model):
    # Агентите, Карактеристиките и Недвижностите се прикажани со нивното име (презиме, површина и опис ако ги имаат, соодветно).
    list_display = ('name',)

    # Агенти и Карактеристики може да бидат додадени само од супер-корисници.
    def has_add_permission(self, request):
        if (request.user.is_superuser):
            return True
        return False


admin.site.register(Feature, FeatureAdmin)


class RealEstateAdmin(admin.ModelAdmin):
    # Агентите, Карактеристиките и Недвижностите се прикажани со нивното име (презиме, површина и опис ако ги имаат, соодветно).
    list_display = ('name', 'location_description', 'area',)

    # Огласи за продажба може да бидат додадени само од агенти
    # и по автоматизам агентот кој додава оглас е еден од задолжените за продажба на таа недвижност.
    def has_add_permission(self, request):
        if Agent.objects.filter(user=request.user).exists():
            return True
        return False

    def save_model(self, request, obj, form, change):
        if Agent.objects.filter(user=request.user).exists():
            obj.agents.add(request.user.agent)
            obj.price = sum(feature.price for feature in obj.features.all())
            obj.save()
        super().save_model(request, obj, form, change)

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        obj = form.instance
        obj.price = obj.calculate_price()
        obj.save()

    # Еден оглас може да биде избришан само ако нема додадено ниту една карактеристика која го опишува.
    def has_delete_permission(self, request, obj=None):
        if obj and obj.features.exists():
            return False
        return True

    # Огласите можат да бидат менувани само од агенти кои се задолжени за продажба на тој оглас,
    # а останатите агенти може само да ги гледаат тие огласи.
    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True

        if Agent.objects.filter(user=request.user).exists() and obj.agents.filter(user=request.user).exists():
            return True
        return False

    # На супер-корисниците во Админ панелот им се прикажуваат само огласите кои се објавени на денешен датум.
    def get_queryset(self, request):
        queryset = super().get_queryset(request)

        if request.user.is_superuser:
            return queryset.filter(published_date=date.today())
        return queryset.filter(agent__user=request.user)


admin.site.register(RealEstate, RealEstateAdmin)
