
from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    listdisplay = ('product_name','price','stock','modified_date','is_available')
    prepopulated_field = {'slug':('product_name',)}


admin.site.register(Product , ProductAdmin)

