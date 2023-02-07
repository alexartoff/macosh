from django.contrib import admin

# Register your models here.
from .models import Service, ServiceImages


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'photo', 'expert', 'price', 'created', 'updated', 'is_published',)
    list_display_links = ('title',)
    ordering = ('id', 'title',)


class ServiceImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'service', 'description', 'alt_text', 'image', 'slug', 'uploaded', 'updated',)
    list_display_links = ('id', 'description', 'alt_text')
    prepopulated_fields = {'slug': ('service',)}
    ordering = ('id', 'service',)


admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceImages, ServiceImagesAdmin)
