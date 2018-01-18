from django.contrib import admin

# Register your models here.
from .models import Order , OrderLineItem

class OrderLineItemAdminInlin(admin.TabularInline):
    model = OrderLineItem
    
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInlin, )
    
admin.site.register(Order, OrderAdmin)