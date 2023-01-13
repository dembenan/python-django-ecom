from django.contrib import admin
from store.models import Cart
from store.models import Order
from store.models import Product

# Register your models here.
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Cart)

