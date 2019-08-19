from django.contrib import admin

from orders.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_driver', 'user_client', 'get_price', 'created_at', 'is_complete']
