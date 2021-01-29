from django.contrib import admin
from .models import Product, Order, AboutUs, Contact
from django.forms import ModelForm




# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['image', 'name', 'description', 'type', 'price']

admin.site.register(Product, ProductsAdmin)

admin.site.register([Order, AboutUs, Contact])
#для того чтобы регистрировали наши модели


