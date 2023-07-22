from django.apps import AppConfig


class ShoppingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shopping'
    def ready(self):
        from django.contrib.auth.models import User
        def get_car_count(self):
            from .models import cart_item
            return cart_item.objects.filter(cart__is_paid = False, cart__user = self).count()
        User.add_to_class("get_cart_count", get_car_count)
