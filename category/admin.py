from django.contrib import admin

from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'show_experts', 'description',)
    list_display_links = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('id',)


# Register your models here.
admin.site.register(Category, CategoryAdmin)
