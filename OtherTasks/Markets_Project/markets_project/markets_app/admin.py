from django.contrib import admin

from markets_app.models import Market, ContactInfo, Employee, Product, ProductMarket


# Register your models here.

# Производите треба да се додаваат во делот за маркети.
class ProductMarketInline(admin.StackedInline):
    model = ProductMarket
    extra = 1


# Не е дозволено додавање и бришење на маркети доколку корисникот не е супер корисник.
# За маркетите во листата се прикажуваат само нивните имиња.
class MarketAdmin(admin.ModelAdmin):
    exclude = ('creator',)
    list_display = ('name',)
    inlines = [ProductMarketInline]

    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        obj.save()

    def has_add_permission(self, request):
        if not request.user.is_superuser:
            return False
        else:
            return True
        # return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        if not request.user.is_superuser:
            return False
        else:
            return True
        # return request.user.is_superuser


admin.site.register(Market, MarketAdmin)


# При креирање на вработен, корисникот се доделува автоматски според најавениот корисник.
# Откако еден вработен ќе биде дефиниран и зачуван,
# истиот може да се промени и избрише само од корисникот кој го креирал вработениот.
# За вработените во листата се прикажуваат нивните имиња и презимиња.
class EmployeeAdmin(admin.ModelAdmin):
    exclude = ('created_by',)
    list_display = ('name', 'surname',)

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()

    def has_change_permission(self, request, obj=None):
        if obj and obj.created_by == request.user:
            return True
        else:
            return False

    def has_delete_permission(self, request, obj=None):
        if obj and obj.created_by == request.user:
            return True
        else:
            return False

    # def save_model(self, request, obj, form, change):
    #     if not change:  # Ако се работи за нов вработен
    #         obj.created_by = request.user  # Постави го тој што е моментално најавен
    #     elif obj.create_by != request.user:  # Ако не е нов вработен, проверка дали тој што е додаден е ист со тој што е моментално најавен
    #         raise PermissionDenied(
    #             "You can't change this Employee.")  # Не е додаден од тој што е моментално најавен, друг корисник пробува
    #     obj.save()


admin.site.register(Employee, EmployeeAdmin)


class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('street', 'street_number', 'phone_number', 'email_address',)


admin.site.register(ContactInfo, ContactInfoAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'is_homemade', 'code',)
    list_filter = ('species', 'is_homemade',)
    search_fields = ('species', 'is_homemade',)


admin.site.register(Product, ProductAdmin)


class ProductMarketAdmin(admin.ModelAdmin):
    list_display = ('product', 'market', 'quantity',)
    list_filter = ('product__species',)


admin.site.register(ProductMarket, ProductMarketAdmin)
