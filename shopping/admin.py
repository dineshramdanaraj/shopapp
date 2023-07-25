from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(item)
admin.site.register(item_category)
admin.site.register(cart)
admin.site.register(UserProfile)
admin.site.register(rating)
admin.site.register(cart_item)
admin.site.register(order)
admin.site.register(coupon)