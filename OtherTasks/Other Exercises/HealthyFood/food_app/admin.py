from django.contrib import admin
from .models import Sale, Product, Client, Category
# Register your models here.

class ProductInlineAdmin(admin.TabularInline):
    model = Product
    exclude = ['user']
    extra = 0

class ProductAdmin(admin.ModelAdmin):
    exclude = ['user']
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(ProductAdmin, self).save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if obj is not None and obj.user != request.user:
            return False
        return super().has_change_permission(request,obj)
    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False


class CategoryAdmin(admin.ModelAdmin):
    inlines = [ProductInlineAdmin]
    list_display = ['name',]
class ClientAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name',]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Sale)