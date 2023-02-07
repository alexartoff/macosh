from django.contrib import admin

# Register your models here.
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'service', 'client_name', 'client_lastname', 'client_email', 'comment', 'order_date', 'is_done')
    list_display_links = ('service', 'client_name', 'client_email',)
    ordering = ('id', 'service', 'client_name', 'client_email',)


admin.site.register(Order, OrderAdmin)
