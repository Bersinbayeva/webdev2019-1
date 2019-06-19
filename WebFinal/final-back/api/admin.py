from django.contrib import admin
from api.models import Product, UserProduct

admin.site.register(UserProduct)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'quantity' 'created_by', )