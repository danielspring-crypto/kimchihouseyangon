from django.contrib import admin
from .models import Order
# Register your models here.
class OrderAdmin(admin.ModelAdmin):
	list_display = ['name', 'count', 'phone', 'cost', 'delivery_fees', 'paid', 'date']
	list_filter = ['count', 'paid','date', 'cost']

admin.site.register(Order, OrderAdmin)
