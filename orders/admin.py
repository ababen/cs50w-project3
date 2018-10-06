from django.contrib import admin

from .models import Orders, Pizza, Toppings, OrderItems

# Register your models here.
admin.site.register(Orders)
admin.site.register(Pizza)
admin.site.register(Toppings)
admin.site.register(OrderItems)