from django.apps import AppConfig


class CakeShopAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "cake_shop_app"

    def ready(self):
        from . import signals
