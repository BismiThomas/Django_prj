from django.contrib import admin
from productapp.models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=('id','name','price','qty','cat','is_vail')
    list_filter=('cat',)
admin.site.register(Product,ProductAdmin)
