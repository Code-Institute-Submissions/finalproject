from django.contrib import admin
from .models import Product,Review, Category
from mptt.admin import DraggableMPTTAdmin

# Register your models here.
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Category, DraggableMPTTAdmin)
# admin.site.register(avgrating)
