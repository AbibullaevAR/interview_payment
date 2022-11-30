from django.contrib import admin


from .models import Currency, Item, Discount, Order
# Register your models here.
admin.site.register(Currency)
admin.site.register(Item)
admin.site.register(Discount)
admin.site.register(Order)
