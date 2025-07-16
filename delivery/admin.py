from django.contrib import admin
from .models import Customer
from .models import Restaurants
from .models import Menu
from .models import Cart
# Register your models here.
admin.site.register(Customer)
admin.site.register(Restaurants)
admin.site.register(Menu)
admin.site.register(Cart)